"""
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
    def set_fuel_efficiency(self):
        self.fuel_efficiency = self.kilometers_per_liter

class WheeledVehicle(FueledVehicleMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

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
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.kilometers_per_liter = kilometers_per_liter
        self.liters_of_fuel_capacity = liters_of_fuel_capacity
