from . import APIError


class JsonParseError(APIError):
    """Raised when there is error parsing JSON."""
    code = 1
    message = 'Error parsing JSON.'
