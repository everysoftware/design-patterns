"""
Identity Map is a design pattern used to manage the identity of objects in a data-driven application.
Its main purpose is to ensure that each object loaded from the database has only one unique copy in the application.

Basics:
* Object caching: When an object is requested, Identity Map first checks if it already exists in memory (in the cache)
for the current session or transaction. If the object is already loaded, then that copy is returned instead of
creating a new instance.

* Maintaining data integrity: This prevents the problem of the same object being loaded multiple times and each
instance having its own state. Instead, all changes to the object will be reflected in a single instance.

* Speeding up data: Since Identity Map stores already loaded objects in the cache, it reduces the need for
repeated database hits, improving performance.
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
