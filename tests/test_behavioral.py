from patterns.behavioral.command import Bank, Account
from patterns.behavioral.interpreter import Subtract, Number, Add
from patterns.behavioral.iterator import NameCollection
from patterns.behavioral.retry import retry


def test_command() -> None:
    bank = Bank()

    account1 = Account("Marcus Aurelius")
    bank.operation(account1, 1000)
    bank.operation(account1, -50)

    account2 = Account("Antoninus Pius")
    bank.operation(account2, 500)
    bank.operation(account2, -100)
    bank.operation(account2, 150)

    assert account1.balance == 950
    assert account2.balance == 550

    bank.undo(3)
    assert account1.balance == 950
    assert account2.balance == 0

    bank.undo(2)
    assert account1.balance == 0
    assert account2.balance == 0


def test_interpreter() -> None:
    expression = Subtract(Number(10), Add(Number(5), Number(3)))
    assert expression.interpret() == 2


def test_iterator() -> None:
    names = NameCollection()
    names.add_name("Alice")
    names.add_name("Bob")
    names.add_name("Charlie")

    # list(names) = [name for name in names]
    assert list(names) == ["Alice", "Bob", "Charlie"]


def test_retry() -> None:
    attempt = 0

    @retry(ConnectionError, attempts=2, delay=0.001)
    def unstable_operation() -> str:
        nonlocal attempt
        attempt += 1
        if attempt < 2:
            raise ConnectionError("Temporary connection error.")
        return "Operation successful!"

    assert unstable_operation() == "Operation successful!"
