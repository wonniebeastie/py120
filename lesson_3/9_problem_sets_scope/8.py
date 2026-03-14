"""
Create a `Car` class that has a class variable named `manufacturer` AND an 
instance variable named `manufacturer`. Initialize these variables to different
values. Add a `show_manufacturer` method that prints both the class and 
instance variables.
"""
class Car:
    manufacturer = 'McDs'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(self.__class__.manufacturer)
        print(self.manufacturer)

car = Car("Hogwarts")
car.show_manufacturer()
# McDs
# Hogwarts
