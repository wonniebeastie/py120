class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
