def test_create_customer(client):
    customer_data = {
        "customer_id": "TEST-1001",
        "full_name": "Test Customer",
        "email": "test.customer1001@example.com",
        "phone": "9876543210",
        "city": "Pune"
    }

    response = client.post(
        "/api/customers/",
        json=customer_data
    )

    assert response.status_code == 201

    data = response.json()

    assert data["customer_id"] == "TEST-1001"
    assert data["full_name"] == "Test Customer"
    assert data["email"] == "test.customer1001@example.com"
    assert data["phone"] == "9876543210"
    assert data["city"] == "Pune"
    assert data["status"] == "Active"