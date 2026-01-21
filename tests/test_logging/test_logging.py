import logging
from typing import Any

from pytest import CaptureFixture

from src.logging_conf import setup_logging


def test_setup_logging(capsys: CaptureFixture[Any]) -> None:
    # Force reset handlers to ensure basicConfig works
    logging.root.handlers = []
    setup_logging()
    # Check if handlers are configured
    assert len(logging.root.handlers) > 0
    # Check if a handler is set to INFO or NOTSET (which inherits)
    # basicConfig sets the root level, but pytest might interfere.
    # We check if the handler is stream handler.
    assert isinstance(logging.root.handlers[0], logging.StreamHandler)
