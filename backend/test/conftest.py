from pathlib import Path
from unittest.mock import AsyncMock, Mock
from budgeting.statement.service import StatementParserService
from fastapi.testclient import TestClient

from budgeting import app
import pytest
from budgeting.services import statement_parser_service

@pytest.fixture
def parser_service_mock():
    async def service_mock():
        return Mock()
    
    return service_mock

@pytest.fixture()
def project_root() -> Path:
    return Path(__file__).parents[1]

@pytest.fixture()
def test_client(
    parser_service_mock: StatementParserService
) -> TestClient:
    
    test_app = app()
    
    fastapi_test_client = TestClient(test_app)
    
    test_app.dependency_overrides[statement_parser_service] = parser_service_mock
    
    return fastapi_test_client

