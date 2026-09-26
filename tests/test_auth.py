def test_register_user(client):
    user_data = {
        "full_name": "Test User",
        "email": "test.user1001@example.com",
        "password": "TestPassword123",
        "phone": "9876543210"
    }

    response = client.post(
        "/api/auth/register",
        json=user_data
    )

    assert response.status_code == 201

    data = response.json()

    assert data["message"] == "Account created successfully."

    user = data["user"]

    assert user["full_name"] == "Test User"
    assert user["email"] == "test.user1001@example.com"
    assert user["phone"] == "9876543210"
    assert user["role"] == "customer"


def test_login_user(client):
    user_data = {
        "full_name": "Login Test User",
        "email": "login.test1001@example.com",
        "password": "TestPassword123",
        "phone": "9876543211"
    }

    register_response = client.post(
        "/api/auth/register",
        json=user_data
    )

    assert register_response.status_code == 201

    login_data = {
        "email": "login.test1001@example.com",
        "password": "TestPassword123"
    }

    response = client.post(
        "/api/auth/login",
        json=login_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Login successful."
    assert data["token_type"] == "bearer"

    assert "access_token" in data
    assert data["access_token"]

    assert data["user"]["email"] == "login.test1001@example.com"
    assert data["user"]["role"] == "customer"


def test_get_current_user(client):
    user_data = {
        "full_name": "Current User Test",
        "email": "current.user1001@example.com",
        "password": "TestPassword123",
        "phone": "9876543212"
    }

    register_response = client.post(
        "/api/auth/register",
        json=user_data
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/auth/login",
        json={
            "email": "current.user1001@example.com",
            "password": "TestPassword123"
        }
    )

    assert login_response.status_code == 200

    login_data = login_response.json()

    access_token = login_data["access_token"]

    assert access_token

    response = client.get(
        "/api/auth/me",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["full_name"] == "Current User Test"
    assert data["email"] == "current.user1001@example.com"
    assert data["phone"] == "9876543212"
    assert data["role"] == "customer"
    assert data["is_active"] is True


def test_login_with_invalid_password(client):
    user_data = {
        "full_name": "Invalid Login Test",
        "email": "invalid.login1001@example.com",
        "password": "CorrectPassword123",
        "phone": "9876543213"
    }

    register_response = client.post(
        "/api/auth/register",
        json=user_data
    )

    assert register_response.status_code == 201

    response = client.post(
        "/api/auth/login",
        json={
            "email": "invalid.login1001@example.com",
            "password": "WrongPassword123"
        }
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Invalid email or password."