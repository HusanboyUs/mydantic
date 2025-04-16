from pydantic import BaseModel
import time

from src import BaseModel as test

class Task(BaseModel):

    name: str
    surname: str

class Student(test):

    name: str
    surname: str


payload = {
    "name": "John",
    "surname": "Usmonov"
}


for x in range(10):
    start = time.perf_counter()
    task = Task(**payload)
    task1 = time.perf_counter() - start

    start = time.perf_counter()
    task = Student(**payload)
    task2 = time.perf_counter() - start

    if task1 > task2:
        print(f"task 1 won in {x}")
    
    elif task2 > task1:
        print(f"task 2 won in {x}")

    else:
        print("Equal")







