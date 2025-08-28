def test_configure_logging_reads_yaml(tmp_path, monkeypatch):
    from utils import configure_logging
    import yaml

    cfg_file = tmp_path / "logging_config.yaml"
    cfg_file.write_text("""
version: 1
formatters:
  simple:
    format: '%(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    stream: ext://sys.stdout
loggers:
  test:
    level: INFO
    handlers: [console]
    propagate: no
root:
  level: INFO
  handlers: [console]
"""
    )

    monkeypatch.chdir(tmp_path)
    config = configure_logging()
    assert isinstance(config, dict)
    assert config.get("version") == 1


def test_constants_headers_values():
    from constants.headers import CONTENT_LENGTH, CONTENT_TYPE, PROCESSING_TIME, APPLICATION_JSON

    assert CONTENT_LENGTH == "content-length"
    assert CONTENT_TYPE == "content-type"
    assert PROCESSING_TIME == "X-Processing-Time"
    assert APPLICATION_JSON == "application/json"


def test_enum_status_contains_expected():
    from enums.status import Status

    assert Status.REG.value == 0
    assert Status.COM.value == 6

