class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            print('Name must be a string.')
        
        if name == '':
            raise ValueError('Name must not be empty')
        
        self._name = name

luna = Person('Luna')
print(luna.name) # Luna

luna.name = 'Luna Lovegood'
print(luna.name) # Luna Lovegood

not_person = Person(56) # Name must be a string.

goku = Person('Goku')
goku.name = '' # ValueError: Name must not be empty
