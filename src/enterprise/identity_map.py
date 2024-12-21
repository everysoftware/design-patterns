"""
Identity Map is a design pattern used to manage the identity of objects in a data-driven application.
Its main purpose is to ensure that each object loaded from the database has only one unique copy in the application.
"""

from abc import ABC, abstractmethod
from typing import Any


class IdentityMap(ABC):
    @abstractmethod
    def get(self, id: Any) -> Any: ...

    @abstractmethod
    def set(self, instance: Any) -> None: ...

    @abstractmethod
    def has(self, id: Any) -> bool: ...
