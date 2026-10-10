from dataclasses import dataclass
from typing import Optional


@dataclass
class MethodType:
    name: str
    id: Optional[int] = None
