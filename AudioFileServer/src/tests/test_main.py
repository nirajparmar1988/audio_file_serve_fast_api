import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.audio_file_server_app.database import Base
from src.audio_file_server_app.main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture
def session(app):

    session = next(get_db())
    Base.metadata.drop_all()
    Base.metadata.create_all()
    yield session
    Base.metadata.drop_all()
    session.commit()

def test_create_and_get_audio_file_song():
    response = client.post(
        "/",
        json={
            "file_type": "song",
            "file_metadata": {"name":"mysong","duration_seconds":520},
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "mysong"
    song_id = data["id"]


    # tes get file here
    file_type = "song"
    response = client.get(f"/{file_type}/{song_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "mysong"
    assert data["id"] == song_id


def test_create_audio_file_podcast():
    response = client.post(
        "/",
        json={
            "file_type": "podcast",
            "file_metadata": {"name":"myPod","duration_seconds":550, "host": "Niraj","participants":"[xyz,abc]"},
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "myPod"
    assert data["host"] == "Niraj"
    pod_id = data["id"]
    # tes get file here
    file_type = "podcast"
    response = client.get(f"/{file_type}/{pod_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "mysong"
    assert data["id"] == pod_id
