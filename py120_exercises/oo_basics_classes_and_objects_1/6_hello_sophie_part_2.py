class Cat:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet() # Hello! My name is Sophie!
