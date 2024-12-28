from pathlib import Path
from fastapi.testclient import TestClient

from budgeting import app
import pytest

@pytest.fixture()
def project_root() -> Path:
    return Path(__file__).parents[1]

@pytest.fixture()
def test_client() -> TestClient:
    return TestClient(app())

