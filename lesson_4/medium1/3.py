class Animal:
    def speak(self, txt):
        print(txt)

class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

kitty = Cat()
kitty.meow() # Meow!
