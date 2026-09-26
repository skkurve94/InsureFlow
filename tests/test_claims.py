def test_create_claim(client):
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

    policy_response = client.post(
        "/api/policies/",
        json=policy_data
    )

    assert policy_response.status_code == 201

    claim_data = {
        "claim_number": "TEST-CLM-1001",
        "policy_number": "TEST-POL-1001",
        "claim_type": "Medical",
        "claim_amount": "75000",
        "claim_date": "2026-09-26",
        "description": "Automated test claim"
    }

    response = client.post(
        "/api/claims/",
        data=claim_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Claim created successfully."

    claim = data["claim"]

    assert claim["claim_number"] == "TEST-CLM-1001"
    assert claim["policy_number"] == "TEST-POL-1001"
    assert claim["claim_type"] == "Medical"
    assert claim["claim_amount"] == 75000
    assert claim["claim_date"] == "2026-09-26"
    assert claim["status"] == "Pending"
    assert claim["description"] == "Automated test claim"