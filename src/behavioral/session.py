"""
Session is a behavioral design pattern that is used to store and manage the state of an object or information
while working with a system. The Session pattern allows you to create an object that acts as a container for
storing data or state required to perform various operations within a single session.
"""

from abc import ABC
from typing import Self, Any


class CloudClient(ABC):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.is_authenticated = False
        self.uploaded_files: set[str] = set()

    def login(self) -> None:
        self.is_authenticated = True

    def logout(self) -> None:
        self.is_authenticated = False

    def upload(self, file_path: str) -> None:
        assert self.is_authenticated
        self.uploaded_files.add(file_path)

    def __enter__(self) -> Self:
        self.login()
        return self

    def __exit__(
        self, exc_type: type[Exception], exc_val: Exception, exc_tb: Any
    ) -> None:
        self.logout()
