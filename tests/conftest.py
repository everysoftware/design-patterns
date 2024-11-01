import logging

import pytest


@pytest.fixture(autouse=True)
def setup_logging() -> None:
    logging.basicConfig(level=logging.INFO)
