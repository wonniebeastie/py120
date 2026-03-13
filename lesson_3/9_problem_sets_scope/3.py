"""
Create a `Cat` class that has a single method named `get_name` that returns the
`name` instance variable. Without initializing `name`, try to instantiate a 
`Cat` object and call `get_name`. Print `Name not set!` when the error occurs.
"""
class Cat:
    def get_name(self):
        return self.name
