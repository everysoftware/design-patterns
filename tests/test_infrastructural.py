from _pytest.logging import LogCaptureFixture

from patterns.infrastructural.client_server import Client, Server
from patterns.infrastructural.reverse_proxy import ReverseProxy


def test_client_server() -> None:
    server = Server()
    client = Client(server)
    client_id = client.add_user("Alice")
    assert client.get_user(client_id) == "Alice"


def test_reverse_proxy(caplog: LogCaptureFixture) -> None:
    server = Server()
    proxy = ReverseProxy(server)
    client = Client(proxy)
    with caplog.at_level("INFO"):
        client_id = client.add_user("Alice")
        assert client.get_user(client_id) == "Alice"
    assert len(caplog.records) == 4
