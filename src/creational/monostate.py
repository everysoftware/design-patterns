"""
The Monostate pattern is a variation of the Singleton pattern where all instances share the same state.

We have been trying to reuse the same instance all this time, but Alex Martelli notes that we should focus on the shared
state and behavior rather than the shared identity. He proposed using the Monostate pattern instead, where there may be
multiple instances, but they share the same state (data).
"""

from typing import Any

from src.creational.db import Database


class Monostate(type):
    _shared_state: dict[str, Any] | None = None

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        obj = super().__call__(*args, **kwargs)
        if cls._shared_state is None:
            cls._shared_state = obj.__dict__
        obj.__dict__ = cls._shared_state
        return obj


class DatabaseMonostate(Database, metaclass=Monostate):
    pass
