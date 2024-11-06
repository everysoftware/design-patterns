"""
Strategy is a behavioral design pattern that allows you to define a family of algorithms, encapsulate them,
and make them interchangeable. The Strategy pattern allows you to change the behavior of an object during program
execution, replacing one algorithm with another without changing the object itself.
"""

from abc import ABC, abstractmethod
from typing import Sequence


class Product:
    def __init__(self, *, price: float = 0, quantity: float = 1) -> None:
        self.quantity = quantity
        self.price = price

    @property
    def total(self) -> float:
        return self.quantity * self.price


class Order:
    def __init__(self, products: Sequence[Product]) -> None:
        self.products = products

    @property
    def total(self) -> float:
        return sum(product.total for product in self.products)


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order: Order) -> float: ...


class RegularShipping(ShippingStrategy):
    def calculate_cost(self, order: Order) -> float:
        return 10


class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, order: Order) -> float:
        return 20


class FreeShipping(ShippingStrategy):
    def calculate_cost(self, order: Order) -> float:
        return 0


class OrderService:
    @staticmethod
    def calculate_total(order: Order, shipping: ShippingStrategy) -> float:
        shipping_cost = shipping.calculate_cost(order)
        return order.total + shipping_cost
