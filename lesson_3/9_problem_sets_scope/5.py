"""
Define a `Student` class that has a class variable named `school_name`. You 
should initialize the school name to `'Oxford'`. After defining the class, 
instantiate an instance of the `Student` class and print the school name using 
that instance.
"""
class Student:
    school_name = 'Oxford'

hairy_potter = Student()

print(hairy_potter.school_name)           # Oxford

# Makes it clearer that it's a class variable
print(hairy_potter.__class__.school_name) # Oxford
