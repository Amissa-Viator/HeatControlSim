import numpy as np
from core.calculation.gradient_method import GradientMethod
from core.calculation.conditional_gradient_method import ConditionalGradientMethod
from core.calculation.utils import collect_all_results
from core.data_worker.data import Data


class ModifiedGradientMethod:
    """
        Implements a projection-iteration modification of gradient-based
        optimization methods using successive grid refinement.

        At each refinement level, the optimal control problem is solved
        on a finer spatial grid. The control approximation obtained on
        the previous grid is interpolated to initialize the next iteration.

        Supports both unconstrained gradient descent and the conditional
        gradient (Frank-Wolfe) method for box-constrained problems.
    """

    def __init__(self, data: Data, v_initial: float, with_condition=False):
        self.data = data
        self.with_condition = with_condition
        self.v_initial = v_initial
        self.modified_gradient = []
        self.modified_functional = []
        self.results = []

    @staticmethod
    def interpolate_values(data: np.ndarray, size: int) -> np.ndarray:
        """
            Transfer the control approximation to a refined grid
            using piecewise linear interpolation.

            Existing grid values are preserved, while new intermediate
            values are computed as averages of adjacent grid points.
        """

        new_v = np.zeros(size)
        new_v[0] = data[0]
        new_v[-1] = data[-1]

        for i in range(1, size - 1):
            old_index = i // 2
            if i % 2 == 0:
                new_v[i] = data[old_index]
            else:
                new_v[i] = (data[old_index] + data[min(old_index + 1, len(data) - 1)]) / 2

        return new_v

    def create_method(self, epsilon, size, alpha, v_values):
        """Create the appropriate gradient-based solver."""

        if self.with_condition:
            return ConditionalGradientMethod(self.data, epsilon, size, alpha, v_values)
        else:
            return GradientMethod(self.data, epsilon, size, alpha, v_values)

    def run(self):
        """
            Solve the optimal control problem on successively refined grids.

            The number of grid intervals doubles at each refinement level.
            The stopping tolerance for the inner optimization method is
            initially proportional to the squared spatial grid step.

            Returns:
                tuple: Numerical results and iteration counts for each
                refinement level.
        """

        coefficient = 10.0
        n = self.data.n_min
        eps = self.data.epsilon
        v_values = None
        total_iterations = []

        while n <= self.data.n_max:
            step = (Data.RIGHT_BORDER - Data.LEFT_BORDER) / n
            epsilon = coefficient * (step ** 2)
            size = n + 1

            # Use the requested tolerance at the final refinement level
            # or when the grid-dependent tolerance becomes smaller.
            if epsilon < eps or n == self.data.n_max:
                epsilon = eps

            # Initialize the control or transfer it from the previous grid.
            if v_values is None:
                v_values = np.full(size, self.v_initial)
            else:
                v_values = self.interpolate_values(v_values, size)

            gm = self.create_method(epsilon, size, self.data.alpha, v_values)
            gm.start()

            total_iterations.append(gm.number_of_iterations)

            values, _ = collect_all_results(self.data, size, gm.x_values, gm.u_values, gm.v_values)
            self.results.append(values)

            self.modified_gradient.append(gm.gradient.copy())
            self.modified_functional.append(gm.functional_list.copy())

            v_values = gm.v_values.copy()
            n *= 2

        return self.results, total_iterations

