class SignalMixin:
    
    def signal_left(self):
        print("Signalling left")

    def signal_right(self):
        print("Signaling right")

    def signal_off(self):
        print("Signal is now off")

class Vehicle:
    counter = 0

    def __init__(self):
        Vehicle.counter += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.counter

class Car(SignalMixin, Vehicle):
    
    def __init__(self):
        super().__init__()

class Truck(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()

class Boat(Vehicle):

    def __init__(self):
        super().__init__()

car1 = Car()
truck1 = Truck()
boat1 = Boat()

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

print(Car.mro())
# [<class '__main__.Car'>, <class '__main__.SignalMixin'>, <class '__main__.Vehicle'>, <class 'object'>]
print(Truck.mro())
# [<class '__main__.Truck'>, <class '__main__.SignalMixin'>, <class '__main__.Vehicle'>, <class 'object'>]
print(Boat.mro())
# [<class '__main__.Boat'>, <class '__main__.Vehicle'>, <class 'object'>]
print(Vehicle.mro()) 
# [<class '__main__.Vehicle'>, <class 'object'>]
