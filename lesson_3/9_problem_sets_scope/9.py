"""
Create a `Bird` class that has an instance attribute, `species`. Create a 
`Sparrow` class that inherits from the `Bird` class. Create a `Sparrow` 
instance object, then print its species. The expected output is `sparrow`.
"""
class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

sparrow1 = Sparrow("Sparrow")
print(sparrow1.species) # Sparrow
