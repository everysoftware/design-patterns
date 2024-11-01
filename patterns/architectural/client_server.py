import uuid
from abc import ABC, abstractmethod
from typing import Any


class IServer(ABC):
    @abstractmethod
    def dispatch(
        self, request_type: str, *args: Any, **kwargs: Any
    ) -> Any: ...


def get_id() -> str:
    return uuid.uuid4().hex


class Server(IServer):
    def __init__(self) -> None:
        self.users: dict[str, str] = {}

    def dispatch(self, request_type: str, *args: Any, **kwargs: Any) -> Any:
        match request_type:
            case "post_user":
                response = self._post_user(*args, **kwargs)
            case "get_user":
                response = self._get_user(*args, **kwargs)
            case _:
                raise ValueError(f"Unknown request type: {request_type}")
        return response

    def _post_user(self, name: str) -> str:
        id = get_id()
        self.users[id] = name
        return self.users[id]

    def _get_user(self, id: str) -> str:
        return self.users[id]


class Client:
    def __init__(self, server: IServer) -> None:
        self.server = server

    def add_user(self, name: str) -> Any:
        user_id = self.server.dispatch("post_user", name)
        print(f"Client: User '{name}' added with ID {user_id}")
        return user_id

    def get_user(self, user_id: str) -> Any:
        user_name = self.server.dispatch("get_user", user_id)
        print(f"Client: User with ID {user_id} is {user_name}")
        return user_name
