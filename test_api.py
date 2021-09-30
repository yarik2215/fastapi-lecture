import pytest
from fastapi import Depends
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


# TODO: Testing
# pytest --disable-warnings

def get_msg():
    raise ValueError("Error")

@app.get("/api")
def some_api(msg = Depends(get_msg)):
    return msg


@pytest.fixture
def mock_dependencies():
    def get_msg_mocked():
        return "Test pass"
    app.dependency_overrides[get_msg] = get_msg_mocked

@pytest.mark.usefixtures("mock_dependencies")
def test_my_api():
    res = client.get("/api")
    assert res.status_code == 200