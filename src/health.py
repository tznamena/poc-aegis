"""Health check endpoint."""


def health_check():
    """Return service health status."""
    return {"status": "ok"}
