"""
Rules:
- if both filling and glazing are `None`, print 'Plain'
- if filling is NOT `None`, just print the filling
- if filling `None`, but glazing is NOT `None`, print 'Plain with {glazing}'
- if both filling and glazing are NOT `None`, print '{filling} with {icing}'

"""
class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    def __str__(self):
        if (self.filling == None) and (self.glazing == None):
            return 'Plain'
        elif self.glazing == None:
            return f'{self.filling}'
        elif self.filling == None:
            return f'Plain with {self.glazing}'
        else:
            return f'{self.filling} with {self.glazing}'

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing
