import logging
import time

from _pytest.logging import LogCaptureFixture

from patterns.structural.composite import Directory, File
from patterns.structural.db import Database
from patterns.structural.decorator import (
    CacheDecorator,
    measure_time,
    log_calls,
)


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


def test_log_calls(caplog: LogCaptureFixture) -> None:
    @log_calls
    def sleep(seconds: float) -> None:
        time.sleep(seconds)

    with caplog.at_level(logging.INFO):
        sleep(0.1)
    assert len(caplog.records) == 2


def test_log_calls_parametrized(caplog: LogCaptureFixture) -> None:
    @log_calls(after=False)
    def sleep(seconds: float) -> None:
        time.sleep(seconds)

    with caplog.at_level(logging.INFO):
        sleep(0.1)
    assert len(caplog.records) == 1


def test_composite() -> None:
    root = Directory("Root")
    file1 = File("File 1.txt")
    file2 = File("File 2.txt")
    folder1 = Directory("Folder 1")
    folder2 = Directory("Folder 2")

    folder1.add(file1)
    folder2.add(file2)
    root.add(folder1)
    root.add(folder2)

    logging.info(root.as_string())

    assert root.children == [folder1, folder2]
