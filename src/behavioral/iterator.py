"""
Iterator is a behavioral design pattern that provides a way to access the elements of an aggregate object sequentially
without exposing its underlying representation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence, Self


class Iterable[T](ABC):
    @abstractmethod
    def __iter__(self) -> Iterator[T]: ...


class Iterator[T](Iterable[T], ABC):
    @abstractmethod
    def __next__(self) -> T: ...


class NameIterator(Iterator[str]):
    def __init__(self, names: Sequence[str]) -> None:
        self._names = names
        self._position = 0

    def __next__(self) -> str:
        if not self._position < len(self._names):
            raise StopIteration
        name = self._names[self._position]
        self._position += 1
        return name

    def __iter__(self) -> Self:
        return self


class NameCollection(Iterable[str]):
    def __init__(self) -> None:
        self._names: list[str] = []

    def add_name(self, name: str) -> None:
        self._names.append(name)

    def __iter__(self) -> NameIterator:
        return NameIterator(self._names)
