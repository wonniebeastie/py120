# Consider the following code:
class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.species = species
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species) # sparrow

"""
Without running the above code, what will it output? If it raises an error, 
explain why and how to fix it.
"""
"""
I think it will raise an error because defining an `__init__` method for 
`Sparrow` causes it to overrid its superclass's `__init__`. And when you create
a `Sparrow` instance, `birdie`, the argument `"sparrow"` is never stored in a
variable inside `Sparrow`'s `__init__`. 

I think could fix it by adding `self.species = species` to it. 
"""
