import pytest

from src.creational.connections import MockConnection
from src.creational.db import (
    Database,
)
from src.creational.di_example import say_hello
from src.creational.monostate import DatabaseMonostate
from src.creational.multiton import DatabaseMultiton
from src.creational.pool import ConnectionPool, EmptyPoolError
from src.creational.singleton import (
    DatabaseInheritedSingleton,
    DatabaseMetaSingleton,
)


@pytest.mark.parametrize(
    "db_type",
    [
        DatabaseInheritedSingleton,
        DatabaseMetaSingleton,
    ],
)
def test_singleton_and_lazy(db_type: type[Database]) -> None:
    # Singleton
    db = db_type(":memory:")
    new_db = db_type(":not_memory:")
    assert db is new_db
    assert db.db_url is new_db.db_url

    # Lazy Initialization
    assert db.connection is db.connection
    assert db.connection is new_db.connection


def test_multiton() -> None:
    # Multiton
    db = DatabaseMultiton(":memory:")
    new_db = DatabaseMultiton(":memory:")
    assert db is new_db

    db2 = DatabaseMultiton(":not_memory:")
    assert db is not db2


def test_monostate() -> None:
    # Monostate
    db = DatabaseMonostate(":memory:")
    new_db = DatabaseMonostate(":not_memory:")
    assert db is not new_db
    assert db.db_url == new_db.db_url


def test_pool() -> None:
    # Object Pool
    with ConnectionPool(MockConnection, 2) as pool:
        with pool.connect() as conn, pool.connect() as conn2:
            assert conn.is_connected
            assert conn2.is_connected
            with pytest.raises(EmptyPoolError):
                with pool.connect():
                    pass
        assert not conn2.is_connected
        assert not conn.is_connected
    assert pool.empty()


def test_di() -> None:
    assert say_hello(1) == "Hello, John!"
