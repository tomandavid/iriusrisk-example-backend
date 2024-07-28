import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine
from sqlalchemy.orm import sessionmaker
from app.models import ChatHistory

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    db = SessionLocal()
    yield db
    db.close()

def test_read_chat_history(client, db, monkeypatch):
    def mock_get_user(credentials):
        return {'id': 'test-user'}

    monkeypatch.setattr('app.auth.supabase.auth.api.get_user', mock_get_user)
    
    # Add mock data to the database
    chat = ChatHistory(
        user_id='test-user',
        thread_id='default-thread',
        user_input='A web application with a database backend and user authentication.',
        response='SQL Injection, Cross-Site Scripting'
    )
    db.add(chat)
    db.commit()

    response = client.get(
        "/chat-history?thread_id=default-thread",
        headers={"Authorization": "Bearer test-token"}
    )
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["user_input"] == "A web application with a database backend and user authentication."
    assert response.json()[0]["response"] == "SQL Injection, Cross-Site Scripting"
