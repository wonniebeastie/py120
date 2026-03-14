"""
Modify the `Student` class from your answer to the previous problem. The 
modified class should have an instance variable called `name` that gets 
initialized during instantiation. Create two `Student` objects with different 
names but the same school, then print the name and school for both students.
"""
class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

student1 = Student("Cthulhu")
student2 = Student("Bambi")

print(student1.name, student1.__class__.school_name) # Cthulu Oxford

# This way makes class variable more obvious
print(student2.name, Student.school_name)            # Bambi Oxford
