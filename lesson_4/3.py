class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

car = Car()
truck = Truck()

car.go_slow() # I am safe and driving slow.
truck.go_very_slow() # I am a heavy truck and like going very slow.

car.go_fast() # I am a super fast Car
truck.go_fast() # I am a super fast Truck
