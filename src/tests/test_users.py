import json

from src.api.users.domain import User


def test_add_user_view(test_app, test_database):
    client = test_app.test_client()
    response = client.post(
        "/users",
        data=json.dumps(
            {
                "username": "a_user_name",
                "email": "email@email.com",
                "first_name": "adam",
                "last_name": "tucker",
                "password": "super_secure_password",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert data.get("message") == "a_user_name was added!"


def create_user_domain_model(username: str, email: str, first_name: str, last_name: str, password: str):
    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password_hash(password=password)
    return user


def test_user_domain_model():
    username = "a_user_name"
    email = "email@email.com"
    first_name = "adam"
    last_name = "tucker"
    password = "super_secure_password"
    user = create_user_domain_model(
        username=username, email=email, first_name=first_name, last_name=last_name, password=password
    )
    assert user.username == username
    assert user.email == email
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.check_password_against_password_hash(password)


def test_user_domain_model_check_password_hash():
    username = "a_user_name"
    email = "email@email.com"
    first_name = "adam"
    last_name = "tucker"
    password = "super_secure_password"
    user = create_user_domain_model(
        username=username, email=email, first_name=first_name, last_name=last_name, password=password
    )
    assert not user.check_password_against_password_hash("not_the_same_password")
