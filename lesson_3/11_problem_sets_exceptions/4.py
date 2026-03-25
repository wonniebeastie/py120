num = float(input('Enter a positive number: '))

if num < 0:
    raise ValueError('The number must be positive.')
print(f'You entered {num}')
