"""Authentication module for gateway."""


def authenticate(username, password):
    """Authenticate a user with username and password."""
    if not username or not password:
        return False
    return _check_credentials(username, password)


def _check_credentials(username, password):
    """Check credentials against the database."""
    # placeholder implementation
    return _validate_password(password)


def validate_token(token):
    """Validate an authentication token."""
    if not token:
        return False
    return len(token) > 10


def _validate_password(password):
    """Validate password strength."""
    return len(password) >= 8
