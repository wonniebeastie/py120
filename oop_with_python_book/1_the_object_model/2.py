class Foo:
    pass

foo = Foo()

print(f'I am a {type(foo).__name__} object')     # I am a Foo object
print(f'I am a {foo.__class__.__name__} object') # I am a Foo object
