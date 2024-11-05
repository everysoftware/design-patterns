"""
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes.
It appears as if the object changed its class. The pattern allows you to get rid of cumbersome conditional statements
such as if and switch, thereby improving the readability and extensibility of the code.

The State pattern represents the different states of an object as separate classes, each with its own behavior
for a specific state. Instead of changing the logic in one class using conditions, states are delegated to the
corresponding objects. When the state of an object changes, the object that handles the requests changes.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Final

RIGHT_PIN: Final[int] = 1234


class ATMContext(ABC):
    cash: int

    @abstractmethod
    def set_state(self, state: ATMState) -> None: ...


class ATMState(ABC):
    def __init__(self, context: ATMContext) -> None:
        self.context = context

    @abstractmethod
    def insert_card(self) -> str: ...
    @abstractmethod
    def enter_pin(self, pin: int) -> str: ...
    @abstractmethod
    def request_cash(self, amount: int) -> str: ...


class NoCard(ATMState):
    def insert_card(self) -> str:
        self.context.set_state(HasCard(self.context))
        return "Card inserted."

    def enter_pin(self, pin: int) -> str:
        return "Insert card first."

    def request_cash(self, amount: int) -> str:
        return "Insert card first."


class HasCard(ATMState):
    def insert_card(self) -> str:
        return "Card already inserted."

    def enter_pin(self, pin: int) -> str:
        if pin != RIGHT_PIN:
            self.context.set_state(NoCard(self.context))
            return "Incorrect PIN."
        self.context.set_state(CorrectPin(self.context))
        return "Correct PIN."

    def request_cash(self, amount: int) -> str:
        return "Enter PIN first."


class CorrectPin(ATMState):
    def insert_card(self) -> str:
        return "Card already inserted."

    def enter_pin(self, pin: int) -> str:
        return "PIN already entered."

    def request_cash(self, amount: int) -> str:
        if amount > self.context.cash:
            self.context.set_state(NoCard(self.context))
            return "Not enough cash."
        self.context.cash -= amount
        self.context.set_state(NoCard(self.context))
        return f"{amount} cash received."


class ATM(ATMContext):
    def __init__(self, cash: int) -> None:
        self.cash = cash
        self.state: ATMState = NoCard(self)

    def set_state(self, new_state: ATMState) -> None:
        self.state = new_state

    def insert_card(self) -> str:
        return self.state.insert_card()

    def enter_pin(self, pin: int) -> str:
        return self.state.enter_pin(pin)

    def request_cash(self, amount: int) -> str:
        return self.state.request_cash(amount)
