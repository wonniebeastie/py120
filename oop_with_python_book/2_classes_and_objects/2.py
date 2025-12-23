"""
Add getter & setter methods using decorators:
- to view & change the color of your car
- add getter method to view but not modify car's model 
- add getter method to view but not modify car's year

Add tests.
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

car1 = Car('Sus Turtle Shell', 5603, 'Rainbow')

# View the color
print(car1.color) # Rainbow

# Change the color
car1.color = 'Turtle Shell Colors'
print(car1.color) # Turtle Shell Colors

# Read-only car's model
print(car1.model) # Sus Turtle Shell

# Read-only car's year
print(car1.year) # 5603
