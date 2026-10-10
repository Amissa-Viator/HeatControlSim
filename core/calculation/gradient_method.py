import numpy as np
from core.calculation.gradient_data import BaseGradientMethod
from core.data_worker.data import Data


class GradientMethod(BaseGradientMethod):
    """
        Implements gradient descent with backtracking step-size reduction
        for an unconstrained optimal control problem.
    """

    def run_algorithm(self):
        count = 0
        next_point = np.zeros(self.size)

        while True:
            if count >= self.MAX_OF_ATTEMPTS:
                print("Max attempts reached")
                break

            self.alpha = self.initial_alpha

            self.calculate_values(self.v_values)
            self.calculate_gradient(self.v_values)
            f_value = self.calculate_functional()
            self.functional_list.append(f_value)

            # Compute the next control approximation along the negative gradient
            next_point = self.v_values - self.alpha * self.gradient

            self.calculate_values(next_point)
            next_f_value = self.calculate_functional()

            # Reduce the step size while the objective does not decrease
            while next_f_value >= f_value and self.alpha > 1e-30:
                self.alpha *= self.MULTIPLIER
                next_point = self.v_values - self.alpha * self.gradient
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
