class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Owner:
    def __init__(self, name):
        self.name = name
        self.adopted_pets = set()

    def add_pet(self, pet):
        self.adopted_pets.add(pet)

    def number_of_pets(self):
        return len(self.adopted_pets)

class Shelter:
    def __init__(self):
        self.shelter_record = {}

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        self.shelter_record[owner] = owner.adopted_pets

    def print_adoptions(self):
        for owner in self.shelter_record:
            print(f"{owner.name} has adopted the following pets:")
            for pet in self.shelter_record[owner]:
                print(f"a {pet.species} named {pet.name}")
            print("")

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
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

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
