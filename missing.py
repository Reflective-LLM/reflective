# A missing class to check if a value is missing,
#     without the need to match data types to None, 0, ""/" ", etc
from typing import Any

class _MissingSentinel:
    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "..."

MISSING: Any = _MissingSentinel()