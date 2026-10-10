import numpy as np
from core.calculation.gradient_data import BaseGradientMethod
from core.data_worker.data import Data


class ConditionalGradientMethod(BaseGradientMethod):
    """
        Implements the conditional gradient (Frank-Wolfe) method
        for an optimal control problem with box constraints.
    """

    def calculate_next_point(self, base, direction, alpha: float) -> np.ndarray:
        """Compute the next control approximation along the feasible direction."""

        return base + alpha * (direction - base)

    def run_algorithm(self):
        count = 0
        next_point = np.zeros(self.size)
        optSolution = np.zeros(self.size)

        v_max = getattr(self.data, "v_max", 1.0)

        while True:
            if count >= self.MAX_OF_ATTEMPTS:
                print("Max attempts reached")
                break

            self.alpha = self.initial_alpha

            self.calculate_values(self.v_values)
            self.calculate_gradient(self.v_values)
            f_value = self.calculate_functional()
            self.functional_list.append(f_value)

            # Solve the linear minimization subproblem over the box constraints
            for i in range(self.size):
                optSolution[i] = Data.V_MIN if self.gradient[i] > 0 else v_max

            next_point = self.calculate_next_point(self.v_values, optSolution, self.alpha)
            self.calculate_values(next_point)
            next_f_value = self.calculate_functional()

            # Reduce the step size while the objective does not decrease
            while next_f_value >= f_value and self.alpha > 1e-30:
                self.alpha *= self.MULTIPLIER
                next_point = self.calculate_next_point(self.v_values, optSolution, self.alpha)
                self.calculate_values(next_point)
                next_f_value = self.calculate_functional()

            self.calculate_gradient(next_point)

            deviation = Data.net_norm_difference(next_point.tolist(),
                                                 self.v_values.tolist(),
                                                 self.step)

            np.copyto(self.v_values, next_point)

            count += 1

            if deviation < self.epsilon:
                break

        self.number_of_iterations = count
