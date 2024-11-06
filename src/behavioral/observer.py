"""
Observer is a behavioral design pattern that is used to create a subscription mechanism that allows objects
to observe and respond to changes in other objects. It is especially useful when you have a single object (the subject)
whose state needs to be monitored and updated by multiple other objects (the observers).

Observer pattern allows you to effectively manage the interaction between objects in the system.
It helps to build a system with one source of changes (subject) and many objects (observers) that react to these
changes, which makes the system flexible, extensible and convenient for adding new functions.
"""

import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# It's like subscriber
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None: ...


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None: ...
    @abstractmethod
    def detach(self, observer: Observer) -> None: ...
    @abstractmethod
    def notify(self) -> None: ...


class TemperatureSensor(Subject):
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temperature = 0.0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
        self.notify()

    def get_temperature(self) -> float:
        return self._temperature


class AirConditioner(Observer):
    def __init__(self) -> None:
        self.temperature = 0.0

    def update(self, temperature: float) -> None:
        self.temperature = temperature
        logger.info(
            f"Air conditioner: The temperature is {self.temperature}°C. Adjusting settings..."
        )


class Heater(Observer):
    def __init__(self) -> None:
        self.temperature = 0.0

    def update(self, temperature: float) -> None:
        self.temperature = temperature
        if self.temperature < 20:
            logger.info("Heater: It's cold! Turning the heater on.")
        else:
            logger.info(
                "Heater: The temperature is comfortable. No need for heating."
            )
