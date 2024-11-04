from abc import ABC, abstractmethod
from typing import Mapping, Any, Self


class Connection(ABC):
    is_connected: bool
    query: str | None

    @abstractmethod
    def connect(self) -> None: ...

    @abstractmethod
    def disconnect(self) -> None: ...

    @abstractmethod
    def execute_query(self, query: str) -> Mapping[str, Any]: ...

    def __enter__(self) -> Self:
        """
        RAII (Resource Acquisition Is Initialization) is a programming idiom that states that, using certain software mechanisms,
        the acquisition of a resource is inextricably linked with initialization, and the release is linked with the destruction of the object.
        """
        self.connect()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.disconnect()


class MockConnection(Connection):
    def __init__(self) -> None:
        self.is_connected = False
        self.query = None

    def connect(self) -> None:
        self.is_connected = True

    def disconnect(self) -> None:
        self.is_connected = False

    def execute_query(self, query: str) -> Mapping[str, Any]:
        self.query = query
        return {"key": "value"}
