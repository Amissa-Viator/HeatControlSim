from dataclasses import dataclass
from typing import Optional


@dataclass
class Files:
    excel_path: str
    phi_plot_path: str
    control_plot_path: str
    distribution_plot_path: str
    id: Optional[int] = None
