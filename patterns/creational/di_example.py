from abc import ABC, abstractmethod

from patterns.creational.di import Container


class IUserManager(ABC):
    @abstractmethod
    def get(self, id: int) -> str: ...


class UserManager(IUserManager):
    def get(self, id: int) -> str:
        return "John"


class UserService:
    def __init__(self, manager: IUserManager):
        self.manager = manager

    def say_hello(self, id: int) -> str:
        return f"Hello, {self.manager.get(id)}!"


container = Container()
container.register(IUserManager, UserManager)
container.register(UserService)


@container.inject
def say_hello(id: int, service: UserService) -> str:
    return service.say_hello(id)
