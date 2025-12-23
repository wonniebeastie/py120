class Cat:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet() # Hello! My name is Sophie!

kitty.name = 'Luna'
kitty.greet() # Hello! My name is Luna!
