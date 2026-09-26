def test_create_policy(client):
    customer_data = {
        "customer_id": "TEST-1001",
        "full_name": "Test Customer",
        "email": "test.customer1001@example.com",
        "phone": "9876543210",
        "city": "Pune"
    }

    customer_response = client.post(
        "/api/customers/",
        json=customer_data
    )

    assert customer_response.status_code == 201

    policy_data = {
        "policy_number": "TEST-POL-1001",
        "customer_id": "TEST-1001",
        "policy_type": "Health Insurance",
        "premium_amount": 15000,
        "coverage_amount": 500000,
        "start_date": "2026-09-26",
        "end_date": "2027-09-25"
    }

    response = client.post(
        "/api/policies/",
        json=policy_data
    )

    assert response.status_code == 201

    data = response.json()

    assert data["policy_number"] == "TEST-POL-1001"
    assert data["customer_id"] == "TEST-1001"
    assert data["policy_type"] == "Health Insurance"
    assert data["premium_amount"] == 15000
    assert data["coverage_amount"] == 500000
    assert data["status"] == "Active"