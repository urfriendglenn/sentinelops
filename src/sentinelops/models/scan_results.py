from dataclasses import dataclass
from datetime import datetime

@dataclass
class ScanResult:
    target: str
    response: int
    server: str
    content_type: str
    last_mod: str
    scan_time: datetime
