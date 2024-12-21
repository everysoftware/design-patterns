"""
Aggregate is an enterprise design pattern that represents the group of dependant domain models.
The main goal is to organize objects, ensure data integrity, and manage complex relationships so that
they remain consistent.
"""

from dataclasses import dataclass


@dataclass
class OrderItem:
    product_id: int
    quantity: int
    price: float

    def total(self) -> float:
        return self.price * self.quantity


@dataclass
class OrderAggregate:
    order_id: int
    items: list[OrderItem]

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def remove_item(self, item: OrderItem) -> None:
        self.items.remove(item)

    def calculate_total(self) -> float:
        return sum(item.total() for item in self.items)
