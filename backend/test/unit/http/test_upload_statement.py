from fastapi.testclient import TestClient


def test_given_valid_statement_upload_expect_successful_api_call(
    test_client: TestClient
):
    response = test_client.post("/statements")
    
    assert response.status_code == 200