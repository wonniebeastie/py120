"""
Add a `get_breed` method to the `Dog` class from your answer to the previous 
problem. The method should return the dog's breed. Use the method to print the 
breeds of the two dog objects you created in the previous problem. You should 
also mark the `breed` instance variable for internal use only.
"""
class Dog:
    def __init__(self, breed):
        self._breed = breed

    @property
    def breed(self):
        return self._breed

doggo1 = Dog('Golden Retriever')
doggo2 = Dog('Poodle')

print(doggo1.breed) # Golden Retriever
print(doggo2.breed) # Poodle
