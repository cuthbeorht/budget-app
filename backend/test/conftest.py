from pathlib import Path
from unittest.mock import AsyncMock, Mock
from fastapi.testclient import TestClient

from budgeting import app
import pytest
from budgeting.services import statement_parser_service

@pytest.fixture()
def project_root() -> Path:
    return Path(__file__).parents[1]

@pytest.fixture()
def test_client() -> TestClient:
    
    test_app = app()
    
    fastapi_test_client = TestClient(test_app)
    
    async def foo():
        pass
    
    test_app.dependency_overrides[statement_parser_service] = foo
    
    return fastapi_test_client

