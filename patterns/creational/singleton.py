from __future__ import annotations

import logging
from abc import ABC
from typing import ClassVar, Any, MutableMapping

from patterns.creational.db import Database

logger = logging.getLogger(__name__)


# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Metaprogramming.html
class InheritedSingleton(ABC):
    """
    Singleton is a creational design pattern that ensures that a class has only one instance and provides a global point of access to it.
    """

    _instance: ClassVar[InheritedSingleton | None] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> InheritedSingleton:
        logger.info(f"{cls.__name__}.__new__ args: {args=}, {kwargs=}")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class MetaSingleton(type):
    _instance: Any | None = None

    def __new__(
        cls,
        name: str,
        bases: tuple[type, ...],
        ns: dict[str, Any],
        **extra: Any,
    ) -> MetaSingleton:
        """Called before the class is created."""
        logger.info(f"{cls.__name__}.__new__ args: {name=}, {bases=}, {ns=}")
        return super().__new__(cls, name, bases, ns)

    def __init__(
        cls,
        name: str,
        bases: tuple[type, ...],
        ns: dict[str, Any],
        **extra: Any,
    ):
        """
        Called after the class is created.

        The primary difference is that when overriding __new__() you can change things like the ‘name’, ‘bases’ and ‘namespace’ arguments before you call the super constructor
        and it will have an effect, but doing the same thing in __init__() you won’t get any results from the constructor call.
        """
        logger.info(
            f"{cls.__name__}.__init__ args: {name=}, {bases=}, {ns=}, {extra=}"
        )
        super().__init__(name, bases, ns)

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Called when the class instance is initialized."""
        logger.info(f"{cls.__name__}.__call__ args: {args=}, {kwargs=}")
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

    @classmethod
    def __prepare__(
        cls, name: str, bases: tuple[type, ...], /, **kwargs: Any
    ) -> MutableMapping[str, object]:
        """Prepare the class namespace. Called when the class code is parsed."""
        logger.info(
            f"{cls.__name__}.__prepare__ args: {name=}, {bases=}, {kwargs=}"
        )
        return super().__prepare__(name, bases, **kwargs)  # noqa


class DatabaseInheritedSingleton(Database, InheritedSingleton):
    pass


class DatabaseMetaSingleton(Database, metaclass=MetaSingleton):
    pass
