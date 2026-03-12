"""
Define a `Dog` class that has a breed instance variable. Instantiate two 
objects from this class, one with the breed `'Golden Retriever'` and another 
with the breed 'Poodle'. Print the breed of each dog.
"""
class Dog:
    def __init__(self, breed):
        self.breed = breed

doggo1 = Dog('Golden Retriever')
doggo2 = Dog('Poodle')

print(doggo1.breed) # Golden Retriever
print(doggo2.breed) # Poodle
