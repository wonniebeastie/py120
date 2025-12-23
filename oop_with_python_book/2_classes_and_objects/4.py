"""
Add a class method to `Car` class that calculates & prints any car's average
gas mileage (miles per gallon). You can compute the mileage by dividing the 
distance traveled (in miles) by the fuel burned (in gallons).
"""
class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0

    def turn_engine_on(self):
        print(f"{self.model}'s engine turns on!")

    def accelerate(self):
        self.speed += 3000
        print(f'You accelerate to {self.speed} mph! Your only wig flies off.')

    def brake(self):
        self.speed -= 1000
        print(f'You slow down to {self.speed} mph.')

    def turn_engine_off(self):
        self.speed = 0
        print(f"{self.model}'s engine turns off.")

    def print_current_speed(self):
        print(f'Your current speed is {self.speed} mph.')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a string')
        
        self._color = color

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    def spray_paint_aqua(self, color):
        self.color = color
        print(f'You spray painted your car to {color}.')

    @classmethod
    def calculate_gas_mileage(cls, miles, gallons):
        mileage = miles / gallons
        print(f'{mileage} miles per gallon')

car1 = Car('Sus Turtle Shell', 5603, 'Rainbow')

Car.calculate_gas_mileage(7809, 4) # 1952.25 miles per gallon
