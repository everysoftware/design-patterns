from typing import Any

from patterns.architectural.client_server import IServer


class ReverseProxy(IServer):
    """
    Reverse Proxy is a structural design pattern that serves as an intermediary between client and server, similar to a traditional proxy.
    While a standard proxy forwards client requests to various servers on behalf of the clients, a reverse proxy does the opposite:
    it receives requests from clients and forwards them to the appropriate servers.

    !!! Forward Proxy — Server which sits in front of clients. Reverse Proxy — Server that sits before the servers.
    """

    def __init__(self, server: IServer) -> None:
        self.server = server

    def dispatch(self, request_type: str, *args: Any, **kwargs: Any) -> Any:
        response = self._forward_request(request_type, *args, **kwargs)
        return self._forward_response(response)

    def _forward_request(self, request_type: str, *args: Any, **kwargs: Any) -> Any:
        print(
            f"Proxy: Forwarding {request_type} request with args {args}, kwargs {kwargs}"
        )
        return self.server.dispatch(request_type, *args, **kwargs)

    @staticmethod
    def _forward_response(response: Any):
        print(f"Proxy: Forwarding response {response} back to client")
        return response
