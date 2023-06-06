class HTTPException(Exception):
    pass


class BadRequest(HTTPException):
    """BadRequest()

    Exception raised for a 400 HTTP status code
    """

    pass


class Unauthorized(HTTPException):
    """Unauthorized()

    Exception raised for a 401 HTTP status code
    """

    pass


class Forbidden(HTTPException):
    """Forbidden()

    Exception raised for a 403 HTTP status code
    """

    pass


class NotFound(HTTPException):
    """NotFound()

    Exception raised for a 404 HTTP status code
    """

    pass


class TooManyRequests(HTTPException):
    """TooManyRequests()

    Exception raised for a 429 HTTP status code
    """

    pass


class InternalServerError(HTTPException):
    """InternalServerError()

    Exception raised for a 5xx HTTP status code
    """

    pass
