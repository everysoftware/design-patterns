from abc import abstractmethod, ABC


class IDatabase(ABC):
    @abstractmethod
    def get(self, id: int) -> str: ...


class Database(IDatabase):
    def get(self, id: int) -> str:
        return "data"


class CachedDatabase(IDatabase):
    """
    Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object,
    allowing you to perform something either before or after the request gets through to the original object.
    """

    def __init__(self) -> None:
        self.cache = {}
        self._proxied = Database()

    def get(self, id: int) -> str:
        if id not in self.cache:
            self.cache[id] = self._proxied.get(id)
        return self.cache[id]
