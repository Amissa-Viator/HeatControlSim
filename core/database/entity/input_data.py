from dataclasses import dataclass
from typing import Optional


@dataclass
class InputData:
    k_expression: str
    phi_expression: str
    f_expression: str
    u0: float
    ul: float
    eps: float
    alpha: float
    v_initial: float
    n_max: int
    n_min: Optional[int] = None
    v_max: Optional[float] = None
    id: Optional[int] = None
