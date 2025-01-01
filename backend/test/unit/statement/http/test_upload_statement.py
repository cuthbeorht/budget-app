from fileinput import filename
from pathlib import Path
from fastapi.testclient import TestClient
import pytest
    
@pytest.fixture()
def empty_statement_contents(
    empty_statement_file: Path
) -> str:
     with open(empty_statement_file, "r") as f:
        return f.read()

def test_given_valid_statement_upload_expect_successful_api_call(
    test_client: TestClient,
    valid_statement_contents: str
):       
    response = test_client.post("/statements/", files={"file": valid_statement_contents})
    
    assert response.status_code == 200
    assert response.json() is None
    
def test_given_empty_statement_upload_execpt_400(
    test_client: TestClient,
    empty_statement_contents: str
):
    response = test_client.post("/statements/", files={"file": empty_statement_contents})
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Error with file upload"}