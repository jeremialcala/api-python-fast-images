from fastapi.testclient import TestClient
import pytest


def test_get_image_from_filename_success(monkeypatch, sample_png_base64):
    from app import app
    import controllers.image as ctr

    # For endpoint /image we need a valid ImageData-like object with PNG
    class Dummy:
        imageData = sample_png_base64
        imageType = "PNG"

    async def fake_get_filename(filename: str):
        return Dummy()

    monkeypatch.setattr(ctr.ImageData, "get_image_from_filename", fake_get_filename)

    client = TestClient(app)
    response = client.get("/image", params={"filename": "Zm9vLnBuZw=="})
    assert response.status_code == 200
    assert response.headers.get("content-type", "").startswith("image/")


def test_get_image_from_uuid(monkeypatch, sample_png_base64):
    from app import app
    import controllers.image as ctr

    class Dummy:
        imageData = sample_png_base64
        imageType = "PNG"

    async def fake_get(uuid):
        return Dummy()

    monkeypatch.setattr(ctr.ImageData, "get_image_from_uuid", fake_get)

    client = TestClient(app)
    response = client.get("/image/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 200
    assert response.headers.get("content-type", "").startswith("image/")

