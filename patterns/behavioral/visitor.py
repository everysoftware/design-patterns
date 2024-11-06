"""
Visitor is a behavioral design pattern that allows you to add new operations to objects without
changing their classes. The Visitor pattern assumes that there is a hierarchy of objects that can be "visited"
by an external object called a visitor, and that various operations defined in the visitor class can be
performed on each object in the hierarchy.

When to use:
* When you need to add new operations to objects, but you can't or don't want to change their classes.
* When you have a hierarchy of objects on which you need to perform various operations, and you need to centralize the logic of these operations.
* When you need to maintain the extensibility of the system by adding new operations without changing the existing class code.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Vehicle(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> Any: ...


class Car(Vehicle):
    def __init__(self, mileage: float = 0) -> None:
        self.mileage = mileage

    def accept(self, visitor: Visitor) -> Any:
        return visitor.visit_car(self)


class Bike(Vehicle):
    def __init__(self, is_mountain: bool = False) -> None:
        self.is_mountain = is_mountain

    def accept(self, visitor: Visitor) -> Any:
        return visitor.visit_bike(self)


class Visitor(ABC):
    @abstractmethod
    def visit_car(self, car: Car) -> Any: ...
    @abstractmethod
    def visit_bike(self, bike: Bike) -> Any: ...


class MaintenanceVisitor(Visitor):
    def visit_car(self, car: Car) -> float:
        base_cost = 100
        additional_cost = car.mileage * 0.1
        return base_cost + additional_cost

    def visit_bike(self, bike: Bike) -> float:
        base_cost = 50
        additional_cost = 10 if bike.is_mountain else 0
        return base_cost + additional_cost
