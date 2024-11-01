"""
Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.

A Decorator is always passed its decorated object. A Proxy might create it himself, or he might have it injected.
"""

import logging
import time
from abc import ABC
from typing import Callable, Literal

from patterns.structural.db import IDatabase


class Decorator(IDatabase, ABC):
    def __init__(self, decorated: IDatabase):
        self._decorated = decorated

    def get(self, id: int) -> str:
        return self._decorated.get(id)

    def set(self, id: int, data: str) -> str:
        return self._decorated.set(id, data)


class CacheDecorator(Decorator):
    def __init__(self, decorated: IDatabase) -> None:
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
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start_time = counter()
            result = func(*args, **kwargs)
            end_time = counter()
            logging.info(
                f"Function {func.__name__} takes {end_time - start_time:.4f} {units}"
            )
            return result

        return wrapper

    return decorator
