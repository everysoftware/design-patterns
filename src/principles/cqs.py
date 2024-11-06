"""
Command-Query Separation (CQS) is a design principle that states that:
a method is either a COMMAND that performs an action OR a QUERY that returns data to the caller, but never both.

CQS focuses on separation of method functions to improve readability and predictability.

Read more:
https://khalilstemmler.com/articles/oop-design-principles/command-query-separation/
https://ru.hexlet.io/courses/python-functions/lessons/command-query-separation/theory_unit
"""


class Account:
    def __init__(self, balance: int = 0) -> None:
        self._balance = balance

    # Command: changes the state of the object (deposits money into the account)
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    # Command: changes the state of the object (withdraws money from the account)
    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    # Query: returns the current balance
    def get_balance(self) -> int:
        return self._balance

    # Query: returns True if the account has enough funds to cover the amount
    def has_funds(self, amount: int) -> bool:
        return self._balance >= amount
