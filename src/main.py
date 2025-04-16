from typing import get_origin, get_args
import typing
import time

from exceptions import FieldValidationError


class BaseModel:
    """Base model for validation"""

    def __init__(self, **kwargs) -> None:
        for key, values in kwargs.items():
            if key in self.__annotations__:
                self.__setattr__(key,values)

        self._validate_field(**kwargs)

    @classmethod
    def _validate_field(cls, **kwargs) -> bool | Exception:
        """Class based method to validate the field types"""

        element = lambda value: kwargs.get(value)

        for native_key, native_type in cls.__annotations__.items():

            current_value = element(native_key)
            if current_value is None:
                raise FieldValidationError(field=f"{native_key}", message=f"{native_key} returned {current_value}")

            if not isinstance(current_value, native_type):
                raise FieldValidationError(field=f"{native_key}", message=f"{native_key} does not much with {current_value} type!")

        return True



