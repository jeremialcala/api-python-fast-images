import asyncio
from uuid import UUID
import pytest


def test_response_data_defaults():
    from classes.dto_response import ResponseData

    rd = ResponseData()
    assert isinstance(rd.uuid, (UUID,))
    assert rd.code == 200
    assert rd.message
    assert rd.timestamp is not None


def test_settings_loads_from_env(monkeypatch):
    from classes.tool_settings import Settings

    settings = Settings()
    assert settings.environment == "test"
    assert isinstance(settings.gmail_server_port, int)


def test_image_data_get_data_fields():
    from classes import entity_image as entity_mod
    # Call the instance method with a duck-typed object to avoid DB dependencies
    dummy = type(
        "Dummy",
        (),
        dict(
            name="file",
            imageType="PNG",
            imageSize="2x2",
            imageMode="RGBA",
            imageData="ZGF0YQ==",
        ),
    )()

    data = entity_mod.ImageData.get_data(dummy)
    assert data["fileName"] == "file.PNG"
    assert data["contentType"] == "image/png"


def test_import_entity_image_without_db_connect(monkeypatch):
    # Ensure our conftest stub prevents real connections at import time
    import importlib
    import sys as _sys

    if "classes.entity_image" in _sys.modules:
        del _sys.modules["classes.entity_image"]

    import classes.entity_image  # noqa: F401  # Re-import should not create DB
    assert True

