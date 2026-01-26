"""
P: keep track of number of pets adopted per owner
P: output which pets owner has adopted
"""
class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Owner:
    def __init__(self, name):
        """
        Each owner should have:
        - a name
        - a list of pets they adopted
        """
        self.name = name
        self.adopted_pets = set()

    def number_of_pets(self):
        """
        O: the number of pets owner instance has
        """
        pass

class Shelter:
    def __init__(self):
        """
        - Each `Shelter` instance should have a masterlist of all owners
          and which pets they adopted
        """
    def adopt(self, owner, pet):
        """
        I: `Owner` instance
        O: `Pet` instance

        Rules:
        - each time someone adopts a pet, their collection of pets should be
          updated
        - the "masterlist" for that `Shelter` instance should be updated
        """
        pass

    def print_adoptions(self):
        """
        Rules:
        - print "masterlist"
        - needs access to:
            - owner
            - their collection of pets

        DS/Brainstorm:
        - 

        Algo:
        - 
        """
        pass

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

shelter.print_adoptions()
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
