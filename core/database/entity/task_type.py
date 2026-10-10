from dataclasses import dataclass
from typing import Optional


@dataclass
class TaskType:
    name: str
    id: Optional[int] = None
