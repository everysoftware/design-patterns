"""
Unit of Work is an enterprise design pattern that maintains a list of objects affected by a business transaction and
coordinates the writing out of changes and the resolution of concurrency problems.
"""

from abc import ABC, abstractmethod
from typing import Self, Any

from src.enterprise.domain_model import Entity
from src.enterprise.source import DataSource
from src.enterprise.specification import Specification


class UnitOfWork(ABC):
    @property
    @abstractmethod
    def source(self) -> DataSource: ...

    @abstractmethod
    def begin(self) -> None: ...

    @abstractmethod
    def add(self, model: Entity) -> None: ...

    @abstractmethod
    def get[T: Entity](self, entity_type: type[T], id: int) -> T | None: ...

    @abstractmethod
    def update(self, model: Entity) -> None: ...

    @abstractmethod
    def delete(self, model: Entity) -> None: ...

    @abstractmethod
    def find[T: Entity](
        self, entity_type: type[T], specification: Specification[T]
    ) -> T | None: ...

    @abstractmethod
    def commit(self) -> None: ...

    @abstractmethod
    def rollback(self) -> None: ...

    def __enter__(self) -> Self:
        self.begin()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()


class MemoryUnitOfWork(UnitOfWork):
    def __init__(self, source: DataSource) -> None:
        self._source = source
        self._new: list[Entity] = []
        self._dirty: list[Entity] = []
        self._removed: list[Entity] = []
        self._all: dict[str, dict[int, Entity]] = {}

    @property
    def source(self) -> DataSource:
        return self._source

    def begin(self) -> None:
        self._source.begin()

    def add(self, model: Entity) -> None:
        self._new.append(model)

    def get[T: Entity](self, entity_type: type[T], id: int) -> T | None:
        data = self._source.get(entity_type.__name__, id)
        if data is None:
            return None
        entity = entity_type(**data)  # noqa
        self._all.setdefault(entity_type.__name__, {})[id] = entity
        return entity

    def update(self, model: Entity) -> None:
        self._dirty.append(model)

    def delete(self, model: Entity) -> None:
        self._removed.append(model)

    def find[T: Entity](
        self, entity_type: type[T], specification: Specification[T]
    ) -> T | None:
        for data in self._source.find_all(entity_type.__name__):
            entity = entity_type(**data)  # noqa
            if specification.is_satisfied_by(entity):
                return entity
        return None

    def commit(self) -> None:
        for model in self._new:
            self._source.insert(model.__class__.__name__, model.__dict__)

        for model in self._dirty:
            self._source.insert(model.__class__.__name__, model.__dict__)

        for model in self._removed:
            self._source.delete(model.__class__.__name__, model.id)

        self._source.commit()

    def rollback(self) -> None:
        self._source.rollback()
        self._new.clear()
        self._dirty.clear()
        self._removed.clear()
