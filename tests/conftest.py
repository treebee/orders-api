from typing import Generator

import pytest
from fastapi.testclient import TestClient

from orders_api.app import create_app


@pytest.fixture()
def app_client() -> Generator[TestClient, None, None]:
    app = create_app()
    yield TestClient(app)
