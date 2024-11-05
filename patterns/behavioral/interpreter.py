"""
Interpreter is a behavioral design pattern that solves the following problem:
Given a language, define a representation for its grammar along with an interpreter that uses the representation
to interpret sentences in the language.
"""

from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self) -> float: ...


class Number(Expression):
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        return self.value


class Add(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()


class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()


if __name__ == "__main__":
    expression = Subtract(Number(10), Add(Number(5), Number(3)))

    result = expression.interpret()
    print("Результат:", result)  # Вывод: Результат: 2
