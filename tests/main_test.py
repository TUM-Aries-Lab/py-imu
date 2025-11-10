"""Test the main function."""

from py_imu.__main__ import main
from py_imu.definitions import DEFAULT_LOG_LEVEL


def test_main() -> None:
    """Test the main function."""
    main(log_level=DEFAULT_LOG_LEVEL, stderr_level=DEFAULT_LOG_LEVEL)
