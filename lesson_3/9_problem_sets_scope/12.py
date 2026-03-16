# Consider the following code:
class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())

# Answer the following question without running the code.
# What will this code output, and why?
