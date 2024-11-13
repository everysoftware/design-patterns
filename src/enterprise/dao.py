"""
DAO (Data Access Object) is an enterprise pattern that is used as abstraction of data persistence.
"""

from abc import ABC, abstractmethod

from src.enterprise.domain_model import User


class UserDAO(ABC):
    @abstractmethod
    def get(self, id: int) -> User | None: ...

    @abstractmethod
    def save(self, user: User) -> User: ...

    @abstractmethod
    def update(self, user: User) -> User: ...

    @abstractmethod
    def delete(self, user: User) -> None: ...

    @abstractmethod
    def get_by_email(self, email: str) -> User | None: ...
