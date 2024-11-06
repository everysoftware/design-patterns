"""
Command (Action, Transaction) is a behavioral design pattern that encapsulate a request as an object,
thereby allowing for the parameterization of clients with different requests, and the queuing or logging of requests.
It also allows for the support of undoable operations.

See more: https://www.youtube.com/watch?v=vER0vYL4hM4
"""

from abc import ABC, abstractmethod


# Receiver (Target)
class Account:
    def __init__(self, name: str, balance: int = 0) -> None:
        self.name = name
        self.balance = balance


class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...


# Command
class Deposit(Command):
    def __init__(self, account: Account, amount: int) -> None:
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.balance += self.amount

    def undo(self) -> None:
        self.account.balance -= self.amount


class Withdraw(Command):
    def __init__(self, account: Account, amount: int) -> None:
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.balance -= self.amount

    def undo(self) -> None:
        self.account.balance += self.amount


# Invoker
class Bank:
    def __init__(self) -> None:
        self.commands: list[Command] = []

    def operation(self, account: Account, amount: int) -> None:
        command_type = Withdraw if amount < 0 else Deposit
        command = command_type(account, abs(amount))
        command.execute()
        self.commands.append(command)

    def undo(self, count: int) -> None:
        assert count <= len(self.commands)
        for _ in range(count):
            command = self.commands.pop()
            command.undo()
