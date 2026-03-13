"""
Create an instance of the `Dog` class from your answer to Problem 2. Set its 
breed directly from outside the class, then print the resulting breed.
"""
class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

doggo = Dog("Panda Dog")
doggo._breed = "Racoon Dog"
print(doggo.get_breed()) # Racoon Dog
