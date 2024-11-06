import logging
import uuid
from abc import ABC, abstractmethod
from typing import Any, Literal, MutableMapping, cast

logger = logging.getLogger(__name__)

RequestType = Literal["post_user", "get_user"]


class IServer(ABC):
    @abstractmethod
    def dispatch(
        self, request_type: RequestType, *args: Any, **kwargs: Any
    ) -> Any: ...


def get_id() -> str:
    return uuid.uuid4().hex


class Server(IServer):
    def __init__(self) -> None:
        self.users: MutableMapping[str, str] = {}

    def dispatch(
        self, request_type: RequestType, *args: Any, **kwargs: Any
    ) -> Any:
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
        return id

    def _get_user(self, id: str) -> str:
        return self.users[id]


class Client:
    def __init__(self, server: IServer) -> None:
        self.server = server

    def add_user(self, name: str) -> str:
        user_id = self.server.dispatch("post_user", name)
        return cast(str, user_id)

    def get_user(self, user_id: str) -> str:
        user_name = self.server.dispatch("get_user", user_id)
        return cast(str, user_name)
