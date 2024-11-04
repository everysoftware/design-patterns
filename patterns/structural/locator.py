from typing import MutableMapping, Any


class UserManager:
    @staticmethod
    def get(id: int) -> str:
        return "John"


class ServiceLocator:
    """
    Inversion of Control (IoC) is a general principle in which dependency management is delegated to a system or external component, rather than being performed by the object itself.
    In this approach, an object does not create its dependencies itself, but receives them from the outside, which is often implemented through DI.
    IoC allows for reduced coupling between components and simplifies testing and replacing individual parts of the system.

    Service Locator is a pattern that creates a single place to register and look up dependencies (services).
    When an object needs a dependency, it calls the Service Locator, which returns the required service initialized before.

    Service locator considered an antipattern because it hides the dependencies of the class, making it harder to understand and test.
    It also makes the class harder to reuse, as it is tightly coupled to the Service Locator.
    """

    def __init__(self) -> None:
        self.services: MutableMapping[type[Any], Any] = {}

    def register[T](self, name: type[T], service: T) -> None:
        self.services[name] = service

    def resolve[T](self, name: type[T]) -> T:
        return self.services[name]  # type: ignore[no-any-return]


locator = ServiceLocator()
locator.register(UserManager, UserManager())


class UserService:
    def __init__(self) -> None:
        self.manager = locator.resolve(UserManager)

    def say_hello(self, id: int) -> str:
        return f"Hello, {self.manager.get(id)}!"


locator.register(UserService, UserService())


def say_hello(id: int) -> str:
    users = locator.resolve(UserService)
    return users.say_hello(id)
