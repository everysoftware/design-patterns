"""
A Future is an object that represents the result of an asynchronous operation. It is used to store the result
    of the operation and notify the caller when the operation is complete.
"""

from __future__ import annotations

from typing import Callable, Generator
from src.concurrency.patterns.coroutine import Awaitable


class Future[T](Awaitable[T]):
    def __init__(self) -> None:
        self._done: bool = False
        self._result: T | None = None
        self._exception: BaseException | None = None
        self._callbacks: list[Callable[[Future[T]], None]] = []

    def done(self) -> bool:
        return self._done

    def result(self) -> T:
        if not self._done:
            raise RuntimeError("Future is not done yet")
        if self._exception:
            raise self._exception
        return self._result  # type: ignore

    def set_result(self, result: T) -> None:
        self._result = result
        self._done = True
        self._schedule_callbacks()

    def set_exception(self, exception: BaseException) -> None:
        self._exception = exception
        self._done = True
        self._schedule_callbacks()

    def add_done_callback(self, callback: Callable[[Future[T]], None]) -> None:
        self._callbacks.append(callback)
        if self._done:
            self._schedule_callbacks()

    def _schedule_callbacks(self) -> None:
        for callback in self._callbacks:
            callback(self)

    def __await__(self) -> Generator[Future[T], None, T]:
        if not self._done:
            yield self
        return self.result()

    __iter__ = __await__
