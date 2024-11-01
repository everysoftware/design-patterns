"""
Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.

A Decorator is always passed its decorated object. A Proxy might create it himself, or he might have it injected.
"""

import functools
import logging
import time
from abc import ABC
from typing import Callable, Literal, overload, TypeVar

from typing_extensions import ParamSpec

from patterns.structural.db import IDatabase

logger = logging.getLogger(__name__)


class IDecorator(IDatabase, ABC):
    def __init__(self, decorated: IDatabase):
        self._decorated = decorated

    def get(self, id: int) -> str:
        return self._decorated.get(id)

    def set(self, id: int, data: str) -> str:
        return self._decorated.set(id, data)


class CacheDecorator(IDecorator):
    def __init__(self, decorated: IDatabase):
        super().__init__(decorated)
        self.cache: dict[int, str] = {}
        self.hit = False

    def get(self, id: int) -> str:
        if id not in self.cache:
            self.cache[id] = super().get(id)
            self.hit = False
        else:
            self.hit = True
        return self.cache[id]


def measure_time[**P, T](
    units: Literal["s", "ns"] = "s",
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    counter = time.perf_counter if units == "s" else time.perf_counter_ns

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start_time = counter()
            result = func(*args, **kwargs)
            end_time = counter()
            logger.info(
                "Function %s takes %s %s",
                func.__name__,
                f"{end_time - start_time:.4f}",
                units,
            )
            return result

        return wrapper

    return decorator


class CallLogger[**P, T]:
    func: Callable[P, T]

    def __init__(
        self, func: Callable[P, T], *, before: bool = True, after: bool = True
    ):
        self.func = func
        self.before = before
        self.after = after

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        if self.before:
            logger.info("Calling %s", self.func.__name__)
        result = self.func(*args, **kwargs)
        if self.after:
            logger.info("Finished %s", self.func.__name__)
        return result


_P = ParamSpec("_P")
_T = TypeVar("_T")


@overload
def log_calls(
    func: Callable[_P, _T],
    *,
    before: bool = True,
    after: bool = True,
) -> Callable[_P, _T]: ...


@overload
def log_calls(
    *,
    before: bool = True,
    after: bool = True,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...


def log_calls(
    func: Callable[_P, _T] | None = None,
    *,
    before: bool = True,
    after: bool = True,
) -> Callable[_P, _T] | Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    def decorator(_func: Callable[_P, _T]) -> Callable[_P, _T]:
        return CallLogger(_func, before=before, after=after)

    if func is not None:
        return decorator(func)
    return decorator
