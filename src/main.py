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


        print(cls.__annotations__)
        print(cls.__dict__)
        print(kwargs)
        _annotations = cls.__annotations__
        
        for native_key, native_type in _annotations.items():

            if native_key not in kwargs.keys():
                if not cls._has_default(key=native_key)[0]:
                    raise FieldValidationError(field=native_key, message=f"{native_key} is not valid in both")



        # for native_key, native_type in cls.__annotations__.items():

        #     current_value = element(native_key)
        #     # if current_value is None:
        #     #     raise FieldValidationError(field=f"{native_key}", message=f"{native_key} returned {current_value}")

        #     if not isinstance(current_value, native_type):
        #         raise FieldValidationError(field=f"{native_key}", message=f"{native_key} does not much with {current_value} typcle!")

        # return True
    

class Students(BaseModel):

    id:int
    #name:str = "Husan"
    surname:str
    #age:int

payload = {
    "id":1,
    "name":"John",
    "surname":"Usmonov",
    "age":19
}


student = Students(**payload)
