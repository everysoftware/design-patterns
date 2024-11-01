from abc import ABC, abstractmethod


class IDatabase(ABC):
    @abstractmethod
    def get(self, id: int) -> str: ...

    @abstractmethod
    def set(self, id: int, data: str) -> str: ...


class Database(IDatabase):
    def __init__(self) -> None:
        self.data: dict[int, str] = {}

    def get(self, id: int) -> str:
        return self.data[id]

    def set(self, id: int, data: str) -> str:
        self.data[id] = data
        return self.data[id]
