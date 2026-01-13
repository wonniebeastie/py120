class Cat:

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

Cat.generic_greeting() # Hello! I'm a cat!

kitty = Cat()
type(kitty).generic_greeting() # Hello! I'm a cat!
