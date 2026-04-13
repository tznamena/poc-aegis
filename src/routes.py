"""Route configuration for gateway."""


ROUTES = {
    "/api/v1/auth": "auth_service",
    "/api/v1/jobs": "controller_service",
    "/api/v1/collections": "hub_service",
    "/api/v1/events": "eda_service",
}


def get_route(path):
    """Resolve a path to its backend service."""
    for prefix, service in ROUTES.items():
        if path.startswith(prefix):
            return service
    return None
