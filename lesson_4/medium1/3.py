class Animal:
    def speak(self, txt):
        print(txt)

class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    def bark(self):
        self.speak('Woof! Woof! Woof!')

kitty = Cat()
kitty.meow() # Meow!

doggo = Dog()
doggo.bark() # Woof! Woof! Woof!
