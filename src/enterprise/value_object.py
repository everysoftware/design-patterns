"""
Value Object is an enterprise design pattern that is used to represent objects that are characterized by their state
(value) rather than identity. This pattern is used to model simple entities that have a value
and do not have an identity of their own.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    postal_code: str
    country: str

    @property
    def full_address(self) -> str:
        return (
            f"{self.street}, {self.city}, {self.postal_code}, {self.country}"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Address):
            return NotImplemented
        return (
            self.street == other.street
            and self.city == other.city
            and self.postal_code == other.postal_code
            and self.country == other.country
        )

    def __hash__(self) -> int:
        return hash((self.street, self.city, self.postal_code, self.country))
