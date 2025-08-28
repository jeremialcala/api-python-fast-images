from fastapi.testclient import TestClient


def test_get_image_from_filename_ok(monkeypatch, sample_png_base64):
    from app import app
    import controllers.image as ctr

    class Dummy:
        imageData = sample_png_base64
        imageType = "PNG"

    async def fake_get(filename: str):
        return Dummy()

    monkeypatch.setattr(ctr.ImageData, "get_image_from_filename", fake_get)

    client = TestClient(app)
    response = client.get("/image", params={"filename": "W0RFMDAxXSBEZWxpbmVhZG9yIEzDrXF1aWRvIFdhdGVyIFJlc2lzdA=="})
    assert response.status_code == 200
