from fastapi.testclient import TestClient

from budgeting import app
import pytest

@pytest.fixture()
def test_client() -> TestClient:
    return TestClient(app())