import inspect
from typing import Callable, MutableMapping, Any


class Container:
    """
    Inversion of Control (IoC) is a general principle in which dependency management is delegated to a system or external component, rather than being performed by the object itself.
    In this approach, an object does not create its dependencies itself, but receives them from the outside, which is often implemented through DI.
    IoC allows for reduced coupling between components and simplifies testing and replacing individual parts of the system.

    Dependency Injection (DI) is a pattern (technique) that allows an object to receive its dependencies from an external source rather than creating them itself.
    DI Container is a class that creates a single place that is responsible for creating and managing the dependencies of an object.
    """

    def __init__(self) -> None:
        self._providers: MutableMapping[type[Any], Callable[[], Any]] = {}

    def register(
        self,
        interface: type[Any],
        implementation: type[Any] | None = None,
    ) -> None:
        impl = implementation if implementation is not None else interface

        def factory() -> Any:
            parameters = inspect.signature(impl).parameters
            args = {
                name: self.resolve(param.annotation)
                for name, param in parameters.items()
                if param.annotation in self._providers
            }
            return impl(**args)

        self._providers[interface] = factory

    def resolve[T](self, interface: type[T]) -> T:
        if interface in self._providers:
            return self._providers[interface]()  # type: ignore[no-any-return]
        raise ValueError(f"No provider registered for {interface}")

    def inject[ReturnT](
        self, func: Callable[..., ReturnT]
    ) -> Callable[..., ReturnT]:
        def wrapper(*args: Any, **kwargs: Any) -> ReturnT:
            annotations = inspect.getfullargspec(func).annotations
            annotations.pop("return", None)
            resolved_args = {
                name: self.resolve(param_type)
                for name, param_type in annotations.items()
                if param_type in self._providers and name not in kwargs
            }
            return func(*args, **resolved_args, **kwargs)

        return wrapper
