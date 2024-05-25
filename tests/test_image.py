from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_image_from_filename_neg():
    response = client.get("image?filename=W0RFMDAxXSBEZWxpbmVhZG9yIEzDrXF1aWRvIFdhdGVyIFJlc2lzdA==")
    assert response.status_code == 200
