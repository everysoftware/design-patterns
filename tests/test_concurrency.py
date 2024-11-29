import time
from typing import Any

from src.concurrency.patterns.coroutine import (
    GeneratorCoroutine,
)
from src.concurrency.patterns.event_loop import run, create_task


# I/O bound task
def sleep(seconds: int) -> GeneratorCoroutine[None, None, None]:
    yield
    start_time = time.time()
    while time.time() - start_time < seconds:
        yield


def get(_url: str) -> GeneratorCoroutine[None, None, str]:
    yield from sleep(1)
    return "OK"


def generate_text() -> GeneratorCoroutine[None, None, str]:
    # health check
    response = yield from get("https://api.openai.com")
    if response != "OK":
        return response
    # generate text
    response = yield from get(
        "https://api.openai.com/generate?prompt=what is the meaning of life?"
    )
    return response


def test_generate_text() -> None:
    assert run(generate_text()) == "OK"


def multiple_generate_text(
    n: int,
) -> GeneratorCoroutine[Any, None, list[str]]:
    yield
    # Load tasks in event queue
    tasks = [create_task(generate_text()) for _ in range(n)]
    responses = []
    # Await tasks
    for task in tasks:
        response = yield from task
        responses.append(response)
    return responses


def test_multiple_generate_text() -> None:
    coro = multiple_generate_text(100)
    assert run(coro) == ["OK"] * 100
