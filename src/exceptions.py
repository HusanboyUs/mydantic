"""File contains custom exceptions for the base class and testing"""


__all__ = ["BaseException", "FieldValidationError"]
__ver__ = 0.1


class BaseException(Exception):
    """Main base exception class"""

    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field} : {message}")


class FieldValidationError(BaseException):
    """Validation Error class"""

    def __init__(self, field, message):
        super().__init__(field, message)
