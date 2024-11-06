"""
Mediator (Intermediary, Controller) is a behavioral design pattern used to simplify interactions between objects.
It reduces the dependency of objects on each other by routing communication through a mediator that
manages the interactions between objects.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Participant:
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator
        self.mediator.add(self)
        self.sent: str | None = None
        self.received: str | None = None

    def send(self, message: str) -> None:
        self.sent = message
        self.mediator.send(self, message)

    def receive(self, message: str) -> None:
        self.received = message


class Mediator(ABC):
    @abstractmethod
    def send(self, sender: Participant, message: str) -> None: ...
    @abstractmethod
    def add(self, participant: Participant) -> None: ...


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.participants: list[Participant] = []

    def add(self, participant: Participant) -> None:
        self.participants.append(participant)

    def send(self, sender: Participant, message: str) -> None:
        for participant in self.participants:
            if participant != sender:
                participant.receive(message)
