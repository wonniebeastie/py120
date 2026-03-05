"""
[] Create methods for ordered comparisons of `Cat` objects by `name` value.
[] Comparison should ignore case.
[] Methods should work for `<`, `<=`, `>`, and `>=` operators.
[] If right-hand operand is not a `Cat` object, return `NotImplemented`.
[] Write test cases to demonstrate viability of methods.
"""
class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() != other.name.casefold()

floof = Cat('Floof')
floof2 = Cat('Floof')
frog_paste = Cat('Frog Paste')

print(floof == frog_paste) # False
print(floof == floof2)     # True

print(floof != frog_paste) # True
print(floof != floof2)     # False


# These test cases are here to show if the right-hand operand is not a `Cat`,
# the methods return `NotImplemented`
print(floof == 'Floof')  # False
print(floof != 'Floof')  # True

floof_lower = Cat('floof')

# Case-insensitive
print(floof == floof_lower) # True
print(floof != floof_lower) # False
