from abc import ABC, abstractmethod
from typing import Sequence

from patterns.creational.jsonable import Jsonable
from patterns.creational.prototype import Cloneable


class Product(Jsonable, Cloneable, ABC):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class Apple(Product):
    def __init__(self, name: str = "apple", price: float = 0.99) -> None:
        super().__init__(name, price)


class Orange(Product):
    def __init__(self, name: str = "orange", price: float = 1.49) -> None:
        super().__init__(name, price)


class Adviser(ABC):
    @abstractmethod
    def suggest(self) -> Sequence[str]: ...


class AppleAdviser(Adviser):
    def suggest(self) -> Sequence[str]:
        return ["apple pie", "cider", "apple juice"]


class OrangeAdviser(Adviser):
    def suggest(self) -> Sequence[str]:
        return ["orange juice", "marmalade", "orange cake"]


class ProductShelf:
    def __init__(self, category: str, products: Sequence[Product]) -> None:
        self.category = category
        self.products = products
