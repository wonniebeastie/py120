class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")

class Cat(Animal):
    def __init__(self, name, age, legs, species, status):
        super().__init__(self, name, age, 4, "cat", status)

    def introduce(self):
        return super().introduce() + 'Meow meow!'
