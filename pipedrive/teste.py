class BaseError(Exception):
    pass


class Forbidden(BaseError):
    def __str__(self) -> str:
        return f"Forbidden: {self.message}"
