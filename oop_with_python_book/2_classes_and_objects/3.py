"""
Add method to the `Car` class that lets you spray paint the car a specific
color. Don't use a setter method. Test code.
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

car1 = Car('Sus Turtle Shell', 5603, 'Rainbow')

car1.spray_paint_aqua('Aquamarine') # You spray painted your car to Aquamarine.
print(car1.color) # Aquamarine
