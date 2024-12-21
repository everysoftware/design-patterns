"""
Repository is an enterprise pattern that mediates between the domain and persistence layers using a collection-like
interface for accessing domain objects.
"""

from abc import ABC, abstractmethod

from src.enterprise.domain_model import User
from src.enterprise.source import DataSource
from src.enterprise.specification import Specification
from src.enterprise.unit_of_work import UnitOfWork


class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None: ...

    @abstractmethod
    def get(self, id: int) -> User | None: ...

    @abstractmethod
    def delete(self, user: User) -> None: ...

    @abstractmethod
    def find(self, specification: Specification[User]) -> User | None: ...


class PersistenceUserRepository(UserRepository):
    def __init__(self, source: DataSource) -> None:
        self.source = source

    def add(self, user: User) -> None:
        if self.get(user.id) is not None:
            self.source.update("User", user.__dict__)
        else:
            self.source.insert("User", user.__dict__)

    def get(self, id: int) -> User | None:
        data = self.source.get("User", id)
        return User(**data) if data else None

    def delete(self, user: User) -> None:
        self.source.delete("User", user.id)

    def find(self, specification: Specification[User]) -> User | None:
        for data in self.source.find_all("User"):
            user = User(**data)
            if specification.is_satisfied_by(user):
                return user
        return None


class CollectionUserRepository(UserRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    def add(self, user: User) -> None:
        self.uow.add(user)

    def get(self, id: int) -> User | None:
        return self.uow.get(User, id)

    def delete(self, user: User) -> None:
        self.uow.delete(user)

    def find(self, specification: Specification[User]) -> User | None:
        return self.uow.find(User, specification)
