from copy import deepcopy
from dataclasses import dataclass
from typing import Callable, Optional
import math
import sympy as sp


@dataclass(frozen=True)
class BoundaryConditions:
    ALPHA_0: float
    ALPHA_1: float
    BETA_0: float
    BETA_1: float
    A: float
    B: float


class Data:
    LEFT_BORDER = 0.0
    RIGHT_BORDER = 1.0
    V_MIN = 0.0

    P_BOUNDARY_CONDITIONS = BoundaryConditions(1, 0, 1, 0, 0, 0)

    def __init__(self, n_max: int, n_min: int, epsilon: float, alpha: float, v_max: float,
                 u_boundary: BoundaryConditions,
                 f: Callable[[float], float] = None,
                 k: Callable[[float], float] = None,
                 phi: Callable[[float], float] = None,
                 k_derivative: Callable[[float], float] = None,
                 f_expr: Optional[sp.Expr] = None,
                 k_expr: Optional[sp.Expr] = None,
                 phi_expr: Optional[sp.Expr] = None):

        self.epsilon = epsilon
        self.n_max = n_max
        self.alpha = alpha
        self.n_min = n_min

        self.v_max = v_max

        self.u_boundary = u_boundary

        self.f = f
        self.k = k
        self.k_derivative = k_derivative
        self.phi = phi

        self.f_expr = f_expr
        self.k_expr = k_expr
        self.phi_expr = phi_expr

    def copy(self):
        return deepcopy(self)

    def k_prime(self, x: float) -> float:
        if self.k_derivative is None:
            return 0.0
        return self.k_derivative(x)

    def integral_function(self, x: float, u: float) -> float:
        return (u - self.phi(x)) ** 2

    def method_simpson(self, x_array, u_array, step: float) -> float:
        n = len(x_array)
        if n < 2:
            return 0.0

        sum_val = self.integral_function(x_array[0], u_array[0]) + self.integral_function(x_array[-1], u_array[-1])

        for i in range(1, n - 1):
            coefficient = 4 if i % 2 == 1 else 2
            sum_val += coefficient * self.integral_function(x_array[i], u_array[i])

        return (step / 3.0) * sum_val

    @staticmethod
    def net_norm_difference(point1, point2, step: float) -> float:
        s = sum((a - b) ** 2 for a, b in zip(point1, point2))
        return math.sqrt(step * s)

    @staticmethod
    def net_norm(values, step: float) -> float:
        s = sum(v ** 2 for v in values)
        return math.sqrt(step * s)
