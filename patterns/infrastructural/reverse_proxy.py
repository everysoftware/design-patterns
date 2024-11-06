"""
Reverse Proxy is a structural design pattern that serves as an intermediary between client and server, similar to a traditional proxy.
While a standard proxy forwards client requests to various servers on behalf of the clients, a reverse proxy does the opposite:
it receives requests from clients and forwards them to the appropriate servers.

!!! Forward Proxy — Server which sits in front of clients. Reverse Proxy — Server that sits before the servers.
"""

import logging
from typing import Any

from patterns.infrastructural.client_server import IServer, RequestType

logger = logging.getLogger(__name__)


class ReverseProxy(IServer):
    def __init__(self, server: IServer) -> None:
        self.server = server

    def dispatch(
        self, request_type: RequestType, *args: Any, **kwargs: Any
    ) -> Any:
        response = self._forward_request(request_type, *args, **kwargs)
        return self._forward_response(response)

    def _forward_request(
        self, request_type: RequestType, *args: Any, **kwargs: Any
    ) -> Any:
        logging.info(
            f"Proxy: Forwarding {request_type} request with args {args}, kwargs {kwargs}"
        )
        return self.server.dispatch(request_type, *args, **kwargs)

    @staticmethod
    def _forward_response(response: Any) -> Any:
        logging.info(f"Proxy: Forwarding response {response} back to client")
        return response
