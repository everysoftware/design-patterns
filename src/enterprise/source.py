from abc import ABC, abstractmethod
from typing import Any, MutableMapping, Sequence

type Row = dict[str, Any]


class DataSource(ABC):
    @abstractmethod
    def insert(self, table: str, data: Row) -> None: ...

    @abstractmethod
    def update(self, table: str, data: Row) -> None: ...

    @abstractmethod
    def get(self, table: str, id: int) -> Row | None: ...

    @abstractmethod
    def delete(self, table: str, id: int) -> None: ...

    @abstractmethod
    def find_all(self, table: str) -> Sequence[Row]: ...

    def begin(self) -> None:
        pass

    def commit(self) -> None:
        pass

    def rollback(self) -> None:
        pass


class Memory(DataSource):
    def __init__(
        self, data: MutableMapping[str, MutableMapping[int, Row]] | None = None
    ) -> None:
        self._data: MutableMapping[str, MutableMapping[int, Any]] = (
            data if data is not None else {}
        )

    def insert(self, table: str, data: Row) -> None:
        self._data[table][data["id"]] = data

    def update(self, table: str, data: Row) -> None:
        self._data[table][data["id"]] = data

    def get(self, table: str, id: int) -> Row | None:
        return self._data[table].get(id)

    def delete(self, table: str, id: int) -> None:
        del self._data[table][id]

    def find_all(self, table: str) -> Sequence[Row]:
        return list(self._data.get(table, {}).values())
