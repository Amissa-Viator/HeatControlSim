from dataclasses import dataclass
from typing import Optional
from core.database.entity.input_data import InputData
from core.database.entity.method_type import MethodType
from core.database.entity.task_type import TaskType


@dataclass
class CalculationSetup:
    input_data: InputData
    task: TaskType
    method: MethodType
    id: Optional[int] = None

