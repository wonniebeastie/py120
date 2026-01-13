class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

kitty = Cat('Sophie')
kitty.personal_greeting()     # Hello! My name is Sophie!
