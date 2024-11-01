from patterns.structural.db import IDatabase, Database


class CachedDatabase(IDatabase):
    """
    Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object,
    allowing you to perform something either before or after the request gets through to the original object.
    """

    def __init__(self) -> None:
        self.cache: dict[int, str] = {}
        self._proxied = Database()

    def get(self, id: int) -> str:
        if id not in self.cache:
            self.cache[id] = self._proxied.get(id)
        return self.cache[id]

    def set(self, id: int, data: str) -> str:
        return self._proxied.set(id, data)
