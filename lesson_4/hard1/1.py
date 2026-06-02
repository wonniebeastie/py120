"""
Goal: Modify the class definitions & move code into a mix-in so that code can
be shared between the wheeled vehicles & `Catamaran`.

Rules:
    - `Auto` represents automobiles
    - `Motorcycles` represent motorcycles
    - `WheeledVehicle` class has common behaviors of `Auto` & `Motocycles`
    - `Catamaran`s don't have tires
    - We still want to track fuel efficiency & range
    - Move code into a mix-in, to share code among the 3 classes

Brainstorm:
    - what we want from all 3
        - `range()`
        - `fuel_efficiency`
        - `fuel_capacity`

Mixin Algo:
    - range
    - set fuel efficiency
    - set fuel capacity
"""
class FueledVehicleMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

    def set_fuel_efficiency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_fuel_capacity(self, liters):
        self.fuel_capacity = liters

class WheeledVehicle(FueledVehicleMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FueledVehicleMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.set_fuel_capacity(liters_of_fuel_capacity)
        self.set_fuel_efficiency(kilometers_per_liter)

auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0
