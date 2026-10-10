from dataclasses import dataclass
from typing import Optional
from core.database.entity.files import Files
from core.database.entity.results import Results


@dataclass
class FilesResults:
    result: Results
    files: Files
    id: Optional[int] = None
