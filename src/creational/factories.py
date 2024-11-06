from abc import ABC, abstractmethod

from src.creational.products import (
    Apple,
    Orange,
    Product,
    Adviser,
    AppleAdviser,
    OrangeAdviser,
)


class ProductSimpleFactory:
    """
    Simple Factory is "fixed", in that you have just one implementation with no subclassing.
    In this case, you will have a class like this.

    Use case: Constructing an Apple or an Orange is a bit too complex to handle in the constructor for either.
    """

    # Here make_apple and make_orange are also implementing the Creational Method pattern.
    @staticmethod
    def make_apple() -> Product:
        product = Apple()
        # ... do some more stuff
        return product

    @staticmethod
    def make_orange() -> Product:
        product = Orange()
        # ... do some more stuff
        return product


def simple_factory_make_product(name: str) -> Product:
    """Or you can have a function that does the same thing:"""
    product: Product
    match name:
        case "apple":
            product = Apple()
            # ... do some more stuff
        case "orange":
            product = Orange()
            # ... do some more stuff
        case _:
            raise ValueError(f"Unknown product: {name}")
    return product


class ProductFactoryMethod(ABC):
    """
    Factory Method is generally used when you have some generic processing in a class,
    but want to vary which kind of fruit you actually use. So:
    """

    @abstractmethod
    def make(self) -> Product: ...


class AppleFactoryMethod(ProductFactoryMethod):
    def make(self) -> Product:
        product = Apple()
        # ... do some more stuff
        return product


class OrangeFactoryMethod(ProductFactoryMethod):
    def make(self) -> Product:
        product = Orange()
        # ... do some more stuff
        return product


class FactoryProvider(ABC):
    """
    Abstract Factory is normally used for things like dependency injection/strategy, when you want to be able to create a whole family of objects that need to be of "the same kind",
    and have some common base classes. Here's a vaguely fruit-related example. The use case here is that we want to make sure that we don't accidentally use an OrangeAdviser on an Apple.
    As long as we get our Maker and Adviser from the same factory, they will match.
    """

    @abstractmethod
    def get_maker(self) -> ProductFactoryMethod: ...

    @abstractmethod
    def get_adviser(self) -> Adviser: ...


class AppleFactoryProvider(FactoryProvider):
    def get_maker(self) -> ProductFactoryMethod:
        return AppleFactoryMethod()

    def get_adviser(self) -> Adviser:
        return AppleAdviser()


class OrangeFactoryProvider(FactoryProvider):
    def get_maker(self) -> ProductFactoryMethod:
        return OrangeFactoryMethod()

    def get_adviser(self) -> Adviser:
        return OrangeAdviser()
