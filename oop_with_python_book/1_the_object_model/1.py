"""
- Classes are created the same way you create a function but by using `class`
instead of `def`.
- Use PascalCase for the class name instead of snake_case.
- You can create an object, or an instance of a class, by calling that class.
"""
class Noodles:
    def __init__(self, name):
        self.name = name

spagehtti = Noodles('Spaghetti')
pho = Noodles('Pho')
ramen = Noodles('Ramen')
