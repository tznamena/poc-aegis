"""Logging configuration for gateway."""

LOG_LEVEL = "INFO"


def setup_logging(level=None):
    """Configure logging for the application."""
    return level or LOG_LEVEL
