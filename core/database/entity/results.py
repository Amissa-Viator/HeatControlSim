from dataclasses import dataclass
from typing import Optional
from core.database.entity.calculation_setup import CalculationSetup


@dataclass
class Results:
    setup: CalculationSetup
    iterations: int
    time_ms: float
    v_norm: float
    functional: float
    gradient_norm: float
    functional_plot_path: str
    rod_plot_path: str
    id: Optional[int] = None
