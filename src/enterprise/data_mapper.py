"""
Data mapper (Persistence/ORM model) is an enterprise design pattern that maps objects to database tables.
"""

from typing import Any


class Column[T]:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...


class User:
    id: Column[int] = Column(auto_increment=True, primary_key=True)
    name: Column[str] = Column()
    email: Column[str] = Column()
    hashed_password: Column[str] = Column()
