class Transform:
    def __init__(self, data):
        self.data = data

    def uppercase(self):
        return self.data.upper()

my_data = Transform('abc')

# Should output:
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
