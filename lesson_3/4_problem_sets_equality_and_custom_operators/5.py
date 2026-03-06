"""
- If both x and y can be expressed as integers, compute the sum of the integer 
values of x and y.
- Otherwise, concatenate the string values of x and y.
"""
"""
I: str or int
O: a Silly object (summed int or concatenated str)

Ex:
- Concatenated:
    - Both are non-numeric strings:
        - Silly('abc') + 'def' ==> Silly('abcdef')

    - self is a non-numeric str & other is an int:
        - Silly('abc') + 123 ==> Silly('abc123')

    - self is an int & other is a non-numeric str:
        - Silly(123) + 'xyz' ==> Silly('123xyz')

- Summed:
    - self is a numeric str & other is an int:
        - Silly('333') + 123 ==> Silly(456)

    - self is an int & other is a numeric str:
        - Silly(123) + '222' ==> Silly(345)

    - Both are ints:
        - Silly(123) + 456 ==> Silly(579)

    - Both are numeric strings:
        - Silly('123') + '456' ==> Silly(579)

Rules:
    - non-numeric string == a string that contains at least one char that's not
      a numeric digit.
    - numeric string == a string that's entirely numeric digits

    - if both x & y are ints or numeric strings:
        - return x + y
    - otherwise:
        - return 'x' + 'y'
    
    - you can't add/concatenate different built-in types
    - 3 cases of self:
        - it's a non-numeric string
        - it's an int
        - it's a numeric string

DS/Brainstorm:
    - __add__ since `Silly` object always appears on the left-hand side in all
      test cases.
    - we need to know if self.value is a non-numeric string, an int, or a 
      numeric str:
        - if it's an int and the other is:
            - a non-numeric str:
                - turn self into a string 
                - concatenate the two
            - a numeric str or an int:
                - turn the other into an int
                - sum them
        - if it's a non-numeric string:
            - turn the other into a str & concatenate the two
        - if it's a numeric str:
            - turn self into an int
            - turn other into an int
            - sum the two

Algo:
    - if helper returns true:
        - turn self into an int
        - turn other into an int 
        - return the sum
    - else:
        - if self is a string of all digits:
            - turn self into an int 
            - turn other into an int
            - return the sum
        - else:
            - turn other into a str
            - return concatenation of self + other

Helper -> Tell if self is an integer or not
    I: self
    O: boolean
    - if self.value is an int, return True
    - else, return False
"""
class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def is_int(self):
        return isinstance(self.value, int)

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)
