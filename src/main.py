from typing import get_origin, get_args
import typing
import time



class BaseModel:
    """Base model for validation"""

    def __init__(self, **kwargs) -> None:
        for key, values in kwargs.items():
            if key in self.__annotations__:
                self.__setattr__(key,values)

        self._validate_field(**kwargs)

    @classmethod
    def _validate_field(cls, **kwargs):
        """Class based method to validate the field types"""

        element = lambda value: kwargs.get(value)

        for native_key, native_type in cls.__annotations__.items():

            current_value = element(native_key)
            if current_value is None:
                print(f"{current_value} is None")
                return False

            if not isinstance(current_value, native_type):
                print(f"{current_value} doesnt match for {native_type}")
                return False

        return True


class Student(BaseModel):

    name: str
    surname: str

payload = {
    "name": "Husan",
    "surname": "Usmonov"
}

start = time.perf_counter()
student = Student(**payload)
print(time.perf_counter() - start)