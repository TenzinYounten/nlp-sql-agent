# app/db/schema_manager.py
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ColumnInfo:
    name: str
    type: str
    description: str
    constraints: List[str] = None

@dataclass
class TableSchema:
    name: str
    columns: List[ColumnInfo]
    description: str = ""