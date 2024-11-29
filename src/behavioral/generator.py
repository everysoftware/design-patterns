"""
Generator is a design pattern to generate objects in a way that allows the client to control the generation process.

Conceptually, an iterator is a mechanism for traversing data element by element, while a generator allows you to
lazily create a result during iteration.

In Python, any function that uses the yield keyword is a generator function. When called, it returns a generator object
that can be used to control the execution of the generator function. The generator object is both an iterator and an
iterable, so you can use it in for loops and pass it to any function that expects an iterable.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from sqlite3 import Connection
from types import TracebackType
from typing import Any, Self, Generator as PythonGenerator

from src.behavioral.iterator import Iterator


# Basic usage


# Type-hinting equivalent to Iterator[int]
def gen_pow(n: int) -> PythonGenerator[int, None, None]:
    yield n**0
    yield n**1
    yield n**2
    yield n**3


# Delegate to another generator
def gen_pow_delegation(n: int) -> PythonGenerator[int, None, None]:
    yield from gen_pow(n)


def count(n: int) -> PythonGenerator[int, None, None]:
    for i in range(n):
        yield i


def count_delegation(n: int) -> PythonGenerator[int, None, None]:
    yield from range(n)


def gen_sum() -> PythonGenerator[int, int, int]:
    total = 0
    while True:
        try:
            value = yield total
            if value is not None:
                total += value
        except StopIteration:
            return total


class CommitException(Exception):
    pass


class AbortException(Exception):
    pass


def db_session(
    db: Connection, sql: str
) -> PythonGenerator[None, tuple[Any, ...], None]:
    cursor = db.cursor()
    try:
        while True:
            try:
                row = yield
                cursor.execute(sql, row)
            except CommitException:
                db.commit()
            except AbortException:
                db.rollback()
    finally:
        db.rollback()


# Class-based generator


class Generator[YieldT, SendT, ReturnT](Iterator[YieldT], ABC):
    @abstractmethod
    def send(self, value: SendT) -> YieldT: ...

    @abstractmethod
    def throw(
        self,
        exc_type: type[BaseException],
        exc_val: BaseException | None = None,
        tb: TracebackType | None = None,
    ) -> Self: ...

    @abstractmethod
    def close(self) -> None: ...


class SumGenerator(Generator[int, int, int]):
    def __init__(self) -> None:
        self._total = 0
        self._closed = False

    def send(self, value: int) -> int:
        if self._closed:
            raise StopIteration(self._total)
        self._total += value
        return self._total

    def throw(
        self,
        exc_type: type[BaseException],
        exc_val: BaseException | None = None,
        tb: TracebackType | None = None,
    ) -> SumGenerator:
        return self

    def close(self) -> None:
        self._closed = True

    def __iter__(self) -> SumGenerator:
        return self

    def __next__(self) -> int:
        return self.send(0)
