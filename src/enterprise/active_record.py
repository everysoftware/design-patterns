"""
Active Record is an enterprise design pattern that allows you to store and retrieve data in a database using objects.
"""

from abc import abstractmethod, ABC
from typing import Self


class User(ABC):
    id: int
    name: str
    email: str
    hashed_password: str

    @abstractmethod
    def save(self) -> None: ...

    @abstractmethod
    def delete(self) -> None: ...

    @abstractmethod
    def get(self, id: int) -> Self: ...
