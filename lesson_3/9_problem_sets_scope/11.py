"""
Create a `Mammal` class that always sets an attribute called `legs` to a value
of `4`. Create a `Human` class that inherits from `Mammal`, but instead sets 
the value of `legs` to `2`. Print the number of legs for a human to verify 
correct operation.
"""
class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

a_human_bean = Human()
print(a_human_bean.legs) # 2
