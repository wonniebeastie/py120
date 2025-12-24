class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    @staticmethod
    def turn_engine_on():
        print('The engine is on!')

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

car1 = Car('Sus Turtle Shell', 5603, 'Rainbow')

car1.turn_engine_on() # The engine is on!
car1.accelerate() # You accelerate to 3000 mph! Your only wig flies off.
car1.print_current_speed() # Your current speed is 3000 mph.
car1.brake() # You slow down to 2000 mph.
car1.print_current_speed() # Your current speed is 2000 mph.
car1.turn_engine_off() # Sus Turtle Shell's engine turns off.
car1.print_current_speed() # Your current speed is 0 mph.

