"""
Specification is an enterprise design pattern that use to describe recombinable business logic in a boolean fashion.
Moreover, this pattern that allows you to combine rules to create more complex rules, which you can use to filter
objects
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

from src.enterprise.domain_model import Entity, User

T = TypeVar("T", bound=Entity)


class Specification(ABC, Generic[T]):
    @abstractmethod
    def is_satisfied_by(self, entity: T) -> bool: ...

    @abstractmethod
    def as_expression(self) -> Any: ...

    def __and__(self, other: Specification[T]) -> Specification[T]:
        return AndSpecification(self, other)

    def __or__(self, other: Specification[T]) -> Specification[T]:
        return OrSpecification(self, other)

    def __invert__(self) -> Specification[T]:
        return NotSpecification(self)


class AndSpecification(Specification[T], Generic[T]):
    def __init__(
        self, spec1: Specification[T], spec2: Specification[T]
    ) -> None:
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, entity: T) -> bool:
        return self.spec1.is_satisfied_by(
            entity
        ) and self.spec2.is_satisfied_by(entity)

    def as_expression(self) -> Any:
        return self.spec1.as_expression() & self.spec2.as_expression()


class OrSpecification(Specification[T], Generic[T]):
    def __init__(
        self, spec1: Specification[T], spec2: Specification[T]
    ) -> None:
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, entity: T) -> bool:
        return self.spec1.is_satisfied_by(
            entity
        ) or self.spec2.is_satisfied_by(entity)

    def as_expression(self) -> Any:
        return self.spec1.as_expression() | self.spec2.as_expression()


class NotSpecification(Specification[T], Generic[T]):
    def __init__(self, spec: Specification[T]) -> None:
        self.spec = spec

    def is_satisfied_by(self, entity: T) -> bool:
        return not self.spec.is_satisfied_by(entity)

    def as_expression(self) -> Any:
        return ~self.spec.as_expression()


class EmailUserSpecification(Specification[User]):
    def __init__(self, email: str) -> None:
        self.email = email

    def is_satisfied_by(self, entity: User) -> bool:
        return entity.email == self.email

    def as_expression(self) -> Any:
        return User.email == self.email


class ActiveUserSpecification(Specification[User]):
    def is_satisfied_by(self, entity: User) -> bool:
        return entity.is_active

    def as_expression(self) -> Any:
        return User.is_active
