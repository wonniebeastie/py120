"""
Modify the `Student` class from your answer to the previous problem. The 
modified class should have a class method that returns the school's name. 
Without instantiating any `Student` objects, print the school's name in two 
different ways: once with the class method, and once by accessing the class 
variable directly.
"""
class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name
