"""
Event Loop is a concurrency design pattern that is used to handle asynchronous events in a program. It is a loop that
listens for events and then triggers the appropriate event handlers. The Event Loop pattern is commonly used in GUI
applications, web servers, and other programs that need to handle multiple events simultaneously.

A Task is a subclass of Future that represents a coroutine that is running in the event loop. It is used to
manage the execution of the coroutine and handle its result.
"""

from __future__ import annotations

import logging
from queue import Queue
from typing import Any

from src.concurrency.patterns.coroutine import GeneratorCoroutine
from src.concurrency.patterns.future import Future

logger = logging.getLogger(__name__)


class Task[T](Future[T]):
    def __init__(
        self, gen: GeneratorCoroutine[Any, Any, T], loop: EventLoop
    ) -> None:
        super().__init__()
        self.gen: GeneratorCoroutine[Any, Any, T] = gen
        self.loop: EventLoop = loop
        loop.put(self)

    def step(self, value: Any = None) -> None:
        # Resume the coroutine
        try:
            yielded = self.gen.send(value)
            # If the coroutine yielded a Future, add a callback to resume the coroutine when the Future is done
            if isinstance(yielded, Future):
                yielded.add_done_callback(lambda fut: self.step(fut.result()))
            else:
                self.loop.put(self)
        # Coroutine has finished
        except StopIteration as e:
            self.set_result(e.value)
        # Coroutine raised an exception
        except Exception as e:
            self.set_exception(e)


class EventLoop:
    def __init__(self) -> None:
        self.q: Queue[Task[Any]] = Queue()

    def put(self, task: Task[Any]) -> None:
        self.q.put(task)

    def run_until_complete[T](
        self, coro: GeneratorCoroutine[Any, Any, T]
    ) -> T:
        task = create_task(coro)
        while not task.done():
            if not self.q.empty():
                next_task = self.q.get()
                next_task.step()
        return task.result()

    def close(self) -> None:
        self.q.queue.clear()


running_loop: EventLoop | None = None


def new_event_loop() -> EventLoop:
    return EventLoop()


def get_running_loop() -> EventLoop | None:
    return running_loop


def get_event_loop() -> EventLoop:
    loop = get_running_loop()
    if loop is not None:
        return loop
    return new_event_loop()


def create_task[T](coro: GeneratorCoroutine[Any, Any, T]) -> Task[T]:
    return Task(coro, get_event_loop())


def run[T](coro: GeneratorCoroutine[Any, Any, T]) -> T:
    global running_loop
    loop = get_event_loop()
    running_loop = loop
    try:
        return loop.run_until_complete(coro)
    finally:
        running_loop = None
        loop.close()
