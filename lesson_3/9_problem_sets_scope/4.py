"""
Create an instance of the `Dog` class from your answer to Problem 2. Set its 
breed directly from outside the class, then print the resulting breed.
"""
class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

doggo1 = Dog('Golden Retriever')
doggo2 = Dog('Poodle')

print(doggo1.get_breed()) # Golden Retriever
print(doggo2.get_breed()) # Poodle
