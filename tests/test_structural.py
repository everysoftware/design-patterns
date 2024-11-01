import logging
import time

from _pytest.logging import LogCaptureFixture

from patterns.structural.db import Database
from patterns.structural.decorator import CacheDecorator, measure_time


def test_cache_decorator() -> None:
    db = CacheDecorator(Database())
    db.set(1, "John")
    db.get(1)
    assert not db.hit
    db.get(1)
    assert db.hit


def test_measure_time(caplog: LogCaptureFixture) -> None:
    @measure_time()
    def sleep(seconds: float) -> None:
        time.sleep(seconds)

    with caplog.at_level(logging.INFO):
        sleep(0.1)
    assert len(caplog.records) == 1
