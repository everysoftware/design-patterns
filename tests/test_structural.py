import logging

from _pytest.logging import LogCaptureFixture

from src.structural.composite import Directory, File
from src.structural.db import Database
from src.structural.decorator import (
    CacheDecorator,
    measure_time,
    tracer,
)
from src.structural.flyweight import FlyweightFactory
from src.structural.locator import say_hello
from src.structural.marker import loggable


def test_cache_decorator() -> None:
    db = CacheDecorator(Database())
    db.set(1, "John")
    db.get(1)
    assert not db.hit
    db.get(1)
    assert db.hit


def test_measure_time(caplog: LogCaptureFixture) -> None:
    @measure_time()
    def plus(x: int, y: int) -> int:
        return x + y

    with caplog.at_level(logging.INFO):
        assert plus(1, 2) == 3
    assert len(caplog.records) == 1


def test_tracer(caplog: LogCaptureFixture) -> None:
    @tracer
    def plus(x: int, y: int) -> int:
        return x + y

    with caplog.at_level(logging.INFO):
        assert plus(1, 2) == 3
    assert len(caplog.records) == 2


def test_tracer_parametrized(caplog: LogCaptureFixture) -> None:
    @tracer(after=False)
    def plus(x: int, y: int) -> int:
        return x + y

    with caplog.at_level(logging.INFO):
        assert plus(1, 2) == 3
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


def test_locator() -> None:
    assert say_hello(1) == "Hello, John!"


def test_flyweight() -> None:
    flyweight = FlyweightFactory()
    soldier1 = flyweight.get_character("soldier")
    soldier1.render("red", 10, 20)

    soldier2 = flyweight.get_character("soldier")
    soldier2.render("blue", 30, 40)

    assert soldier1 is soldier2


def test_marker() -> None:
    @loggable
    def plus(x: int, y: int) -> int:
        return x + y

    assert loggable.is_marked(plus)
