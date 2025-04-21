""" This file contains only unittests for BaseModel """

from unittest import TestCase
#module under test
from src import BaseModel
from src import FieldValidationError


class Task(BaseModel):

    id:int
    title: str
    content: str
    is_published: bool = False


class TestBaseModelInitiations(TestCase):

    def test_model_initiation_variables(self):
        test_task_object = Task(
            id=1,
            title = "My First Task",
            content="My task is to write a tests",
            is_published = False
        )
        self.assertEqual(test_task_object.id) == Task.id
        self.assertEqual(test_task_object.title) == Task.title
        self.assertEqual(test_task_object.content) == Task.content
    
    def test_model_default_values(self):
        test_task_object = Task(
            id=1,
            title = "My First Task",
            content="My task is to write a tests",
            is_published = True
        )
        self.assertFalse(test_task_object.is_published)

    def test_missing_values(self):
        with self.assertRaises([FieldValidationError]):
            test_task_object = Task(
            id=1,
            content="My task is to write a tests",
            is_published = True
        )
        
    def test_check_fiel_types(self):
        with self.assertRaises([FieldValidationError]) as errorMessage:
            test_task_object = Task(
                id='1',
                title = "My First Task",
                content="My task is to write a tests",
                is_published = True
            )
        
        self.assertEqual(errorMessage.msg,f'id did not match with str')
