from typing import get_origin, get_args
import typing
import time

from exceptions import FieldValidationError


class BaseModel:
    """Base model for validation"""

    def __init__(self, **kwargs) -> None:
        for key, values in kwargs.items():
            if key in self.__annotations__:
                has_default = self._has_default(key=key)
                if has_default[0]:
                    self.__setattr__(key,has_default[1])
                else:
                    self.__setattr__(key,values)

        self._validate_fields(**kwargs)
    
    @classmethod
    def _has_default(cls, key) -> list[bool,str:None]:
        """Checks if class variable has a default value assigned, returns True if it has False otherwise"""
        if key not in cls.__dict__:
            return [False]
        return [True, cls.__dict__[key]]
    
    @classmethod
    def _validate_fields(cls, **kwargs) -> bool | Exception:
        """Class based method to validate the field types"""

        _external_values = kwargs

        for native_key, native_type in cls.__annotations__.items():

            # checking surface level only -> doesnt work for values inside of nested dicts
            if native_key not in kwargs.keys():
                if not cls._has_default(key=native_key)[0]:
                    raise FieldValidationError(
                        field=native_key, 
                        message=f"Given field -> {native_key} is defined in class but not provided in payload"
                    )
            
            # print(f" args: {get_args(native_type)} for {native_type} {native_key}")
            # print(f" origin: {get_origin(native_type)} for {native_type} {native_key}")

            #if nested - checking only type of the values in nested list
            if get_origin(native_type):

                for value in cls.__annotations__.get(native_key):
                    print(f"Value is ------------------- {value}")
                    if not isinstance(value, dict):
                        pass

                    if any(isinstance(value, t) and isinstance(value, t) for t in native_key):
                        pass

                

                break

            # if not nested
            if not isinstance(_external_values.get(native_key), native_type):
                raise FieldValidationError(
                        field=_external_values.get(native_key),
                        message=f"{_external_values.get(native_key)} did not match with {native_type}")
