"""
Template method is a behavioral design pattern that defines the skeleton of an algorithm in an operation,
deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm
without changing the algorithm's structure.
"""

import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class Beverage(ABC):
    @abstractmethod
    def brew(self) -> None: ...

    @staticmethod
    def boil_water() -> None:
        logger.info("Boiling water...")

    @staticmethod
    def pour_in_cup() -> None:
        logger.info("Pouring into the cup...")

    def prepare_beverage(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()


class Tea(Beverage):
    def brew(self) -> None:
        logger.info("Steeping the tea...")


class Coffee(Beverage):
    def brew(self) -> None:
        logger.info("Brewing coffee...")
