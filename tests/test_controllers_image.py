import asyncio
import types
import pytest


@pytest.fixture
def dummy_image(sample_png_base64):
    class Dummy:
        imageData = sample_png_base64
        imageType = "PNG"

    return Dummy()


def test_ctr_get_image_data_from_uuid_success(monkeypatch):
    import controllers.image as ctr

    async def fake_get(uuid):
        return object()

    monkeypatch.setattr(ctr.ImageData, "get_image_from_uuid", fake_get)

    result = asyncio.get_event_loop().run_until_complete(
        ctr.ctr_get_image_data_from_uuid(uuid="00000000-0000-0000-0000-000000000000")
    )
    assert result is not None


def test_ctr_get_image_data_from_uuid_exception(monkeypatch):
    import controllers.image as ctr

    async def fake_get(uuid):
        raise RuntimeError("boom")

    monkeypatch.setattr(ctr.ImageData, "get_image_from_uuid", fake_get)

    result = asyncio.get_event_loop().run_until_complete(
        ctr.ctr_get_image_data_from_uuid(uuid="00000000-0000-0000-0000-000000000000")
    )
    assert result is None


def test_ctr_get_image_data_from_filename_found(monkeypatch, dummy_image):
    import controllers.image as ctr

    async def fake_get(filename: str):
        return dummy_image

    monkeypatch.setattr(ctr.ImageData, "get_image_from_filename", fake_get)

    result = asyncio.get_event_loop().run_until_complete(
        ctr.ctr_get_image_data_from_filename(filename="Zm9vLnBuZw==")
    )
    assert result is dummy_image


def test_ctr_get_image_data_from_filename_not_found(monkeypatch):
    import controllers.image as ctr
    from fastapi import HTTPException

    async def fake_get(filename: str):
        return None

    monkeypatch.setattr(ctr.ImageData, "get_image_from_filename", fake_get)

    with pytest.raises(HTTPException) as exc:
        asyncio.get_event_loop().run_until_complete(
            ctr.ctr_get_image_data_from_filename(filename="bm90LWZvdW5kLnBuZw==")
        )
    assert exc.value.status_code == 404


def test_ctr_stream_image_from_data(monkeypatch, dummy_image):
    import controllers.image as ctr
    from fastapi.responses import StreamingResponse

    result = asyncio.get_event_loop().run_until_complete(
        ctr.ctr_stream_image_from_data(dummy_image)
    )
    assert isinstance(result, StreamingResponse)
    assert result.media_type == "image/png"

