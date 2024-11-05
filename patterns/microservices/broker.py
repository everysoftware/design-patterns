"""
The Broker pattern is a microservice pattern. Its main goal is to organize and simplify interactions between different components of the system by using an intermediary
that manages communication. The broker helps structure the application architecture by providing centralized management of interactions and message routes between services.

Broker is like bidirectional proxy.
"""

from abc import ABC, abstractmethod


class IService(ABC):
    @abstractmethod
    def receive(self, message: str) -> None: ...

    @abstractmethod
    def send(self, message: str, to: str) -> None: ...


class IBroker(ABC):
    @abstractmethod
    def register(self, name: str, service: IService) -> None: ...

    @abstractmethod
    def propagate(
        self, from_service: str, message: str, to_service: str
    ) -> None: ...


class Service(IService):
    @property
    def service_name(self) -> str:
        return self.__class__.__name__

    def __init__(self, broker: IBroker) -> None:
        self.broker = broker
        self.broker.register(self.service_name, self)

    def send(self, message: str, to: str) -> None:
        print(f"{self.service_name}: Sending message '{message}' to {to}")
        self.broker.propagate(self.service_name, message, to)

    def receive(self, message: str) -> None:
        print(f"{self.service_name}: Received message '{message}'")


class Broker(IBroker):
    def __init__(self) -> None:
        self.services: dict[str, IService] = {}

    def register(self, name: str, service: IService) -> None:
        self.services[name] = service
        print(f"Broker: Registered {name}")

    def propagate(
        self, from_service: str, message: str, to_service: str
    ) -> None:
        print(
            f"Broker: Forwarding message from {from_service} to {to_service}"
        )
        if to_service in self.services:
            self.services[to_service].receive(message)
        else:
            print(f"Broker: Service {to_service} not found")


class UserService(Service):
    pass


class OrderService(Service):
    pass
