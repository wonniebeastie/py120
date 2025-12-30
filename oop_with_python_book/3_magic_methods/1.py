class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.color.capitalize()} {self.year} {self.model}'

    def __repr__(self):
        color = repr(self.color)
        year = repr(self.year)
        model = repr(self.model)
        return f'Car({model}, {year}, {color})'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')
