"""
Create a `Cat` class that has a single method named `get_name` that returns the
`name` instance variable. Without initializing `name`, try to instantiate a 
`Cat` object and call `get_name`. Print `Name not set!` when the error occurs.
"""
class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            print('Name not set!')

kitty1 = Cat()
kitty1.get_name()  # Name not set!
