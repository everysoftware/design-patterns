"""
Aggregate is an enterprise design pattern that represents the group of dependant domain models.
The main goal is to organize objects, ensure data integrity, and manage complex relationships so that
they remain consistent.

Basics
* Root Entity: An aggregate has a root entity, which is the access point to all other objects in the aggregate.
* Coupled entities: All objects within an aggregate are tightly coupled and should be considered a single logical unit.
* Data Integrity: Changes within an aggregate must be made through the root entity to maintain data integrity.

Domain model can be considered as an aggregate if it satisfies the conditions above, e.g. User.
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
