import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models import ChatHistory
from app.schemas.auth import User
from app.services.threat_scenario import get_db
from app.auth import verify_token, supabase

# Mock the database session
@pytest.fixture(scope="function")
def mock_db_session():
    session = MagicMock(spec=Session)
    session.query.return_value.filter_by.return_value.all.return_value = [
        ChatHistory(user_id="test-user", thread_id="test-thread", user_input="Input", response="Output")
    ]
    return session

# Patch the dependency that provides the database session
@pytest.fixture(scope="function")
def mock_get_db(mocker, mock_db_session):
    return mocker.patch('app.services.threat_scenario.get_db', return_value=iter([mock_db_session]))

# Fixture to mock the supabase.auth.get_user dependency
@pytest.fixture(scope="function")
def mock_verify_token(mocker):
    mock_get_user = mocker.patch('app.auth.supabase.auth.get_user', return_value=User(id="test-user"))
    app.dependency_overrides[verify_token] = lambda: User(id="test-user")
    return mock_get_user

# Client to make requests to the FastAPI application
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_generate_threat_scenarios_no_token(client, mock_get_db):
    response = client.post(
        "/generate-threat-scenarios",
        json={"message": "A web application with a database backend and user authentication."}
    )
    assert response.status_code == 403

def test_generate_threat_scenarios_invalid_input(client, mock_get_db, mock_verify_token):
    response = client.post(
        "/generate-threat-scenarios",
        json={},
        headers={"Authorization": "Bearer valid-token"}
    )
    assert response.status_code == 422

def test_generate_threat_scenarios(client, mock_get_db, mock_verify_token):
    response = client.post(
        "/generate-threat-scenarios",
        json={"message": "A web application with a database backend and user authentication."},
        headers={"Authorization": "Bearer valid-token"}
    )
    assert response.status_code == 200


