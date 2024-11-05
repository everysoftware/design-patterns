"""
Iterator is a behavioral design pattern that provides a way to access the elements of an aggregate object sequentially
without exposing its underlying representation.
"""

from abc import ABC, abstractmethod
from typing import Any, Sequence, Self


class Iterator(ABC):
    @abstractmethod
    def __next__(self) -> Any: ...
    @abstractmethod
    def has_next(self) -> bool: ...
    @abstractmethod
    def __iter__(self) -> Self: ...


class NameIterator(Iterator):
    def __init__(self, names: Sequence[str]) -> None:
        self._names = names
        self._position = 0

    def __next__(self) -> str:
        if not self.has_next():
            raise StopIteration
        name = self._names[self._position]
        self._position += 1
        return name

    def has_next(self) -> bool:
        return self._position < len(self._names)

    def __iter__(self) -> Self:
        return self


class Iterable(ABC):
    @abstractmethod
    def __iter__(self) -> Iterator: ...


class NameCollection(Iterable):
    def __init__(self) -> None:
        self._names: list[str] = []

    def add_name(self, name: str) -> None:
        self._names.append(name)

    def __iter__(self) -> NameIterator:
        return NameIterator(self._names)
