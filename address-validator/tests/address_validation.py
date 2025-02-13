import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app() 
    app.config["TESTING"] = True  
    with app.test_client() as client:
        yield client 

def test_valid_address(client):
    response = client.post("/validate/address", json={
        "address": "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore, Karnataka",
        "pincode": "560050"
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "Valid"

def test_invalid_pincode(client):
    response = client.post("/validate/address", json={
        "address": "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore, Karnataka",
        "pincode": "560095"
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "Invalid"

def test_no_pincode_provided(client):
    response = client.post("/validate/address", json={
        "address": "80 Feet Rd, Banashankari, Bangalore, Karnataka"
    })
    data = response.get_json()
    assert response.status_code == 400
    assert data["status"] == "Error"

def test_invalid_pincode_format(client):
    response = client.post("/validate/address", json={
        "address": "80 Feet Rd, Banashankari, Bangalore, Karnataka",
        "pincode": "56005"
    })
    data = response.get_json()
    assert response.status_code == 400
    assert "error" in data  

def test_no_address(client):
    response = client.post("/validate/address", json={})
    data = response.get_json()
    assert response.status_code == 400
    assert "error" in data  