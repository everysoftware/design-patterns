"""
Null object is a behavioral design pattern that helps to avoid null references by providing a default object.
The goal of this pattern is to avoid null checks and simplify code by providing a "neutral" implementation that
does nothing but has the same behavior and interface as regular objects.
"""

import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None: ...


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        logger.info(message)


class NullLogger(Logger):
    def log(self, message: str) -> None:
        pass


class App:
    def __init__(self, log: Logger) -> None:
        self.logger = log

    def run(self) -> None:
        self.logger.log("Application has started.")
