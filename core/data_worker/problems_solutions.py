from enum import Enum


class ProblemType(Enum):
    WITHOUT_CONSTRAINT = 1
    WITH_CONSTRAINT = 2


class SolutionMethod(Enum):
    GRADIENT_METHOD = 1
    MODIFIED_METHOD = 2
    CONDITIONAL_GRADIENT_METHOD = 3
    COMPARE_MODIFIED_TO_GRADIENT = 4
