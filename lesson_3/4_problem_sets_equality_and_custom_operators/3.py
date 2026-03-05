"""
[x] Create methods for ordered comparisons of `Cat` objects by `name` value.
[x] Comparison should ignore case.
[x] Methods should work for `<`, `<=`, `>`, and `>=` operators.
[x] If right-hand operand is not a `Cat` object, return `NotImplemented`.
[x] Write test cases to demonstrate viability of methods.
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

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() < other.name.casefold()

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() > other.name.casefold()

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() <= other.name.casefold()

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() >= other.name.casefold()

floof = Cat('Floof')
floof2 = Cat('Floof')
frog_paste = Cat('Frog Paste')

print(floof < frog_paste)  # True
print(floof > frog_paste)  # False
print(floof < floof2)      # False

print(floof <= frog_paste) # True
print(frog_paste <= floof) # False
print(floof <= floof2)     # True

print(floof > frog_paste) # False
print(frog_paste > floof) # True
print(floof > floof2)     # False

print(floof >= frog_paste) # False
print(frog_paste >= floof) # True
print(floof >= floof2)     # True
