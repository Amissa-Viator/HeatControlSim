from abc import ABC, abstractmethod
from typing import List
import numpy as np
from core.calculation.finite_difference import FiniteDifference
from core.data_worker.data import Data


class BaseGradientMethod(ABC):
    """
        Abstract base class for gradient-based optimal control methods.

        Provides numerical evaluation of the state and adjoint variables,
        the objective functional, and its gradient.

        Concrete subclasses implement the corresponding optimization
        algorithm and stopping criterion.
    """

    MAX_OF_ATTEMPTS: int = 100000
    MULTIPLIER: float = 0.5

    def __init__(
        self,
        data: Data,
        epsilon: float,
        size: int,
        alpha: float,
        v: List[float]
    ):
        self.data = data
        self.size = int(size)
        self.step = (Data.RIGHT_BORDER - Data.LEFT_BORDER) / (self.size - 1)
        self.epsilon = float(epsilon)

        self.x_values = np.zeros(self.size)
        self.u_values = np.zeros(self.size)
        self.p_values = np.zeros(self.size)
        self.v_values = np.array(v, dtype=float).copy()
        self.gradient = np.zeros(self.size)

        self.functional_list: List[float] = []

        self.initial_alpha = float(alpha)
        self.alpha = float(alpha)
        self.number_of_iterations = 0

    def calculate_values(self, v: np.ndarray) -> None:
        """
            Solve the state and adjoint boundary value problems
            for the given control approximation.
        """

        u_solver = FiniteDifference(
            self.size,
            list(v),
            self.data.u_boundary,
            False,
            self.data
        )
        x_vals, u_vals = u_solver.start()
        self.x_values = np.array(x_vals)
        self.u_values = np.array(u_vals)

        p_solver = FiniteDifference(
            self.size,
            list(self.u_values),
            Data.P_BOUNDARY_CONDITIONS,
            True,
            self.data
        )
        _, p_vals = p_solver.start()
        self.p_values = np.array(p_vals)

    def calculate_gradient(self, _v: np.ndarray) -> None:
        """Compute the functional gradient from the adjoint solution."""

        self.gradient = 2.0 * self.p_values

    def calculate_functional(self) -> float:
        """Evaluate the objective functional using Simpson's rule."""

        return self.data.method_simpson(self.x_values, self.u_values, self.step)

    @abstractmethod
    def run_algorithm(self) -> None:
        pass

    def start(self):
        """
            Execute the optimization algorithm and update the final
            state, adjoint, gradient, and functional values.
        """
        self.run_algorithm()

        self.calculate_values(self.v_values)
        self.calculate_gradient(self.v_values)
        self.functional_list.append(self.calculate_functional())

    @property
    def get_gradient(self) -> np.ndarray:
        return self.gradient

    @property
    def get_number_of_iterations(self) -> int:
        return self.number_of_iterations

    @property
    def get_functional_list(self) -> List[float]:
        return self.functional_list

    @property
    def get_x_values(self) -> np.ndarray:
        return self.x_values

    @property
    def get_u_values(self) -> np.ndarray:
        return self.u_values

    @property
    def get_v_values(self) -> np.ndarray:
        return self.v_values

    @property
    def get_step(self) -> float:
        return self.step
