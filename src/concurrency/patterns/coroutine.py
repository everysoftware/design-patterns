from abc import abstractmethod, ABC
from typing import Any, Generator


GeneratorCoroutine = Generator


class Awaitable[T](ABC):
    @abstractmethod
    def __await__(self) -> Generator[Any, Any, T]: ...


class AwaitableCoroutine[YieldT, SendT, ReturnT](
    Awaitable[ReturnT], Generator[YieldT, SendT, ReturnT], ABC
):
    @abstractmethod
    def __await__(self) -> Generator[YieldT, SendT, ReturnT]: ...
