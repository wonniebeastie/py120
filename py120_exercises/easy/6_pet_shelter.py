"""
P: keep track of number of pets adopted per owner
P: output which pets owner has adopted

Rules:
 - need a method called `print_adoptions` in `Shelter` class
 - in the print statements:
    - `owner.name` has to be accessed
    - `number_of_pets` method has to be called on owner instance
        - the number of pets is tied to each `Owner` instance
- only 1 `Shelter` instance is needed
- `shelter.adopt` is called each time for each adopted pet
    - pet can only be adopted once? (but dunno if this is even needed)

DS/Brainstorm:
 - `print_adoptions` means -> gather pets in a collection & print them
    - f-string
    - new line
 - `number_of_pets` can just return the length of that collection
 - each `Owner` instance can have a collection of pets that grows overtime
    - each time `shelter.adopt` is called for that instance:
        - add the pet instance to that collection?
 - So.... I want:
    - a collection (should go in `Owner`)
    - to print that collection's length (should go in `Shelter`)
"""

class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Owner:
    def __init__(self, name):
        self.name = name
        self.adopted_pets = set()

    def number_of_pets(self):
        return len(self.adopted_pets)

class Shelter:
    def adopt(self, owner, pet):
        owner.adopted_pets.add(pet)

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

print(phanson.adopted_pets)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")

# The outputs we want:
# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.
