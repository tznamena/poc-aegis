"""Authentication module for gateway."""


def authenticate(username, password):
    """Authenticate a user with username and password."""
    if not username or not password:
        return False
    return _check_credentials(username, password)


def _check_credentials(username, password):
    """Check credentials against the database."""
    # placeholder implementation
    return True
