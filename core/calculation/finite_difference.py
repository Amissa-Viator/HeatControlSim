import numpy as np
from typing import List
from core.data_worker.data import Data, BoundaryConditions

class FiniteDifference:
    """
        Solves one-dimensional linear boundary value problems using
        the finite difference method on a uniform spatial grid.

        The resulting tridiagonal linear system is solved using
        the Thomas algorithm (tridiagonal matrix algorithm).

        The right-hand side depends on whether the state or
        adjoint boundary value problem is being solved.
    """

    def __init__(self, size: int, functions: List[float],
                 conditions: BoundaryConditions, is_seek_p_value: bool,
                 data: Data):

        self.data = data
        self.SIZE = size
        self.STEP = (Data.RIGHT_BORDER - Data.LEFT_BORDER) / (size - 1)

        self.x_values = np.linspace(Data.LEFT_BORDER, Data.RIGHT_BORDER, size)
        self.values = np.zeros(size)
        self.functions = np.array(functions)

        self.conditions = conditions
        self.is_p_value_seek = is_seek_p_value

    def start(self):
        """Solve the boundary value problem and return grid nodes and values."""

        self.finite_difference_method()
        return self.x_values, self.values

    def finite_difference_method(self):
        """Assemble and solve the finite difference system."""

        N = self.SIZE
        h = self.STEP
        x = self.x_values
        f_vals = self.functions

        a = np.zeros(N)
        b = np.zeros(N)
        c = np.zeros(N)
        d = np.zeros(N)

        # Assemble the tridiagonal system at interior grid nodes.
        b[0] = self.conditions.ALPHA_0 - self.conditions.ALPHA_1 / h
        c[0] = self.conditions.ALPHA_1 / h
        d[0] = self.conditions.A

        b[N - 1] = self.conditions.BETA_0 + self.conditions.BETA_1 / h
        a[N - 1] = -self.conditions.BETA_1 / h
        d[N - 1] = self.conditions.B

        # Construct the right-hand side for the adjoint or state equation.
        for i in range(1, N - 1):
            k_i = self.data.k(x[i])
            k_der_i = self.data.k_prime(x[i])

            a[i] = k_i - h * k_der_i / 2
            b[i] = -2 * k_i
            c[i] = k_i + h * k_der_i / 2

            if self.is_p_value_seek:
                d[i] = h**2 * (self.data.phi(x[i]) - f_vals[i])
            else:
                d[i] = -h**2 * (self.data.f(x[i]) + f_vals[i])

        self.tridiagonal_solve(a, b, c, d)

    def tridiagonal_solve(self, a, b, c, d):
        """
            Solve a tridiagonal linear system using the Thomas algorithm.

            The forward sweep computes modified coefficients, while
            backward substitution reconstructs the numerical solution.
        """

        n = len(b)
        cp = np.zeros(n)
        dp = np.zeros(n)

        cp[0] = c[0] / b[0]
        dp[0] = d[0] / b[0]

        for i in range(1, n):
            denom = b[i] - a[i] * cp[i - 1]
            if denom == 0.0:
                raise ZeroDivisionError("Division by zero in tri-diagonal solver")

            cp[i] = c[i] / denom if i < n - 1 else 0.0
            dp[i] = (d[i] - a[i] * dp[i - 1]) / denom

        self.values[-1] = dp[-1]
        for i in reversed(range(n - 1)):
            self.values[i] = dp[i] - cp[i] * self.values[i + 1]
