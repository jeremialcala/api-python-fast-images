import os
import base64
import pytest
import sys

# Stub mongoengine.connect before any model imports to avoid real DB connections
try:
    import mongoengine  # type: ignore

    def _fake_connect(*args, **kwargs):
        return None

    mongoengine.connect = _fake_connect  # type: ignore[attr-defined]
except Exception:
    pass


# Set required environment variables for Settings before modules import
os.environ.setdefault("client_id", "test-client")
os.environ.setdefault("national_id_url", "http://localhost")

os.environ.setdefault("db_name", "testdb")
os.environ.setdefault("db_host", "mongodb://localhost:27017")
os.environ.setdefault("db_username", "user")
os.environ.setdefault("db_password", "pass")

os.environ.setdefault("sender_email", "sender@example.com")
os.environ.setdefault("sender_password", "secret")

os.environ.setdefault("gmail_server_url", "smtp.gmail.com")
os.environ.setdefault("gmail_server_port", "587")

os.environ.setdefault("expiration_time", "3600")
os.environ.setdefault("activation_code_length", "6")
os.environ.setdefault("password_length", "12")

os.environ.setdefault("qms_server", "http://qms.local")
os.environ.setdefault("qms_user", "qmsuser")
os.environ.setdefault("qms_password", "qmspass")
os.environ.setdefault("queue_name", "queue")
os.environ.setdefault("amqp_exchange", "amq.direct")
os.environ.setdefault("amqp_routing_key", "route")

os.environ.setdefault("key_size", "2048")
os.environ.setdefault("private_key_filename", "priv.pem")
os.environ.setdefault("public_key_filename", "pub.pem")

os.environ.setdefault("environment", "test")
os.environ.setdefault("version", "0.0.0")


@pytest.fixture()
def sample_png_base64():
    try:
        from PIL import Image
    except Exception:
        pytest.skip("Pillow not installed")

    import io

    image = Image.new("RGBA", (2, 2), (255, 0, 0, 255))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    encoded = base64.b64encode(buffer.read()).decode("utf-8")
    return encoded

