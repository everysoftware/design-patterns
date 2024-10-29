from typing import Self, ClassVar, Any

from patterns.creational.db import Database


class InheritedSingleton:
    """
    A singleton is a creational design pattern that ensures that a class has only one instance and provides a global point of access to it.
    """

    _instance: ClassVar[Self | None] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        print(f"__new__ args: {args=}, {kwargs=}")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class MetaSingleton(type):
    _instance: ClassVar[Self | None] = None

    def __new__(cls, name: str, bases: tuple[type, ...], dct: dict[str, Any]) -> Self:
        """Called when the class is defined."""
        print(f"__new__ args: {name=}, {bases=}, {dct=}")
        return super().__new__(cls, name, bases, dct)

    def __call__(cls: type[Self], *args: Any, **kwargs: Any) -> Self:
        """Called when the class instance is created."""
        print(f"__call__ args: {args=}, {kwargs=}")
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class DatabaseInheritedSingleton(Database, InheritedSingleton):
    pass


class DatabaseMetaSingleton(Database, metaclass=MetaSingleton):
    pass
