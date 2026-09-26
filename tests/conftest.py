import os

import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.database import Base, get_db
from app.main import app


TEST_DATABASE_URL = "sqlite:///./test_insureflow.db"


@pytest.fixture
def client():
    if os.path.exists("test_insureflow.db"):
        os.remove("test_insureflow.db")

    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()

        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    test_client = TestClient(app)

    try:
        yield test_client

    finally:
        app.dependency_overrides.clear()

        test_client.close()

        engine.dispose()

        if os.path.exists("test_insureflow.db"):
            os.remove("test_insureflow.db")