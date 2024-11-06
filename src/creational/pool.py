"""
An object pool is a creational design pattern, a set of initialized and ready-to-use objects.

When the system needs an object, it is not created, but taken from the pool. When the object is no longer needed,
it is not destroyed, but returned to the pool.

An object pool is used to improve performance when creating an object at the beginning of the work and destroying
it at the end leads to high costs.
The performance improvement is especially noticeable when objects are frequently created and destroyed,
but only a small number of them exist at a time.
"""

import queue
from abc import abstractmethod, ABC
from typing import Self, Any

from src.creational.connections import Connection


class EmptyPoolError(Exception):
    pass


class Pool(ABC):
    @abstractmethod
    def connect(self) -> Connection: ...

    @abstractmethod
    def disconnect(self, connection: Connection) -> None: ...

    @abstractmethod
    def dispose(self) -> None: ...

    @abstractmethod
    def empty(self) -> bool: ...


class ConnectionPool(Pool):
    def __init__(self, connection_class: type[Connection], pool_size: int = 5):
        self.pool: queue.Queue[Connection] = queue.Queue(maxsize=pool_size)
        self.connection_class = connection_class

        # Fill the pool with connections
        for _ in range(pool_size):
            conn = connection_class()
            self.pool.put(conn)

    def connect(self) -> Connection:
        try:
            connection = self.pool.get_nowait()
            return connection
        except queue.Empty:
            raise EmptyPoolError from None

    def disconnect(self, connection: Connection) -> None:
        self.pool.put(connection)

    def dispose(self) -> None:
        while True:
            try:
                conn = self.pool.get_nowait()
                conn.disconnect()
            except queue.Empty:
                break

    def empty(self) -> bool:
        return self.pool.empty()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.dispose()
