"""
Delegate is a structural design pattern is used to delegate responsibility for a task from one object to another.
This pattern helps create a flexible architecture where tasks can be delegated between objects while maintaining low
coupling and high modularity.
"""

from abc import abstractmethod, ABC


class IPrinter(ABC):
    @abstractmethod
    def print(self, document: str) -> str: ...


class InkJetPrinter(IPrinter):
    def print(self, document: str) -> str:
        return f"InkJet printing {document}"


class LaserPrinter(IPrinter):
    def print(self, document: str) -> str:
        return f"Laser printing {document}"


class Printer:
    def __init__(self, delegate: IPrinter):
        self.delegate = delegate

    def print_doc(self, document: str) -> str:
        return self.delegate.print(document)
