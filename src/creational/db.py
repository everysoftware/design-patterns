from typing import Any

from src.creational.connections import Connection, MockConnection


class Database:
    _connection: Connection | None = None

    def __init__(self, db_url: str) -> None:
        self.db_url = db_url

    @property
    def connection(self) -> Any:
        """
        Lazy Initialization allows an object to be created only when it is needed.
        """
        if not self._connection:
            self._connection = MockConnection()
        return self._connection
