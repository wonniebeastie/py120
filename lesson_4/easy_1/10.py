class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

cat1 = Cat('Tubby')
print(Cat.cats_count()) # 1

cat2 = Cat('Meowth')
print(Cat.cats_count()) # 2

cat3 = Cat('Munchkin')
print(Cat.cats_count()) # 3
