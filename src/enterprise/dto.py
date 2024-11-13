"""
DTO (Data Transfer Object) is an enterprise pattern that is used as abstraction of data transfer between layers.

DTOs are often simple objects that do not contain any business logic.
They are used to transfer data between different layers of an application, such as between
the presentation layer and the business logic layer.
"""

from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    name: str
    email: str


@dataclass
class UserCreateDTO:
    name: str
    email: str
    password: str


@dataclass
class UserChangePasswordDTO:
    old_password: str
    new_password: str


@dataclass
class UserChangeEmailDTO:
    email: str


@dataclass
class UserUpdateDTO:
    name: str | None = None
