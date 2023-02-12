import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_account(client):
    # send a request to the endpoint to create an account
    response = client.post("/accounts", json={"balance": 100.0})

    # verify the response status code is 201 (created)
    assert response.status_code == 201

    # verify the response body contains the correct data
    data = response.json()
    assert data["balance"] == 100.0
    return data["id"]

def test_get_account(client, account_id):
    # send a request to the endpoint to retrieve an account
    response = client.get(f"/accounts/{account_id}")

    # verify the response status code is 200 (OK)
    assert response.status_code == 200

    # verify the response body contains the correct data
    data = response.json()
    assert data["balance"] == 100.0

def test_transfer_money(client, source_id, target_id):
    # send a request to the endpoint to transfer money
    response = client.post("/transfers", json={"source_id": source_id, "target_id": target_id, "amount": 50.0})

    # verify the response status code is 200 (OK)
    assert response.status_code == 200

    # verify the response body contains the correct data
    data = response.json()
    assert data["detail"] == "Transfer successful"

    # retrieve the updated account information
    response = client.get(f"/accounts/{source_id}")
    data = response.json()
    assert data["balance"] == 150.0
