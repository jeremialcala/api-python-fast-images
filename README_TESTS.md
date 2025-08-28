# Running the Test Suite

- Python 3.13 (already available in the container)
- No external services are required. MongoDB is stubbed in tests.

```bash
# One-time setup
cd /workspace
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# If venv/pip is missing
sudo apt-get update -y && sudo apt-get install -y python3-venv python3-pip

# Run tests
pytest -q
```

Notes:
- Environment variables required by `classes.Settings` are set in `tests/conftest.py` for isolation.
- `mongoengine.connect` is stubbed in `tests/conftest.py` to avoid real DB connections.
- `httpx` is pinned to a version compatible with `starlette`'s `TestClient`. 