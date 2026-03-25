try:
    dividend = float(input('Enter the dividend: '))
    divisor = float(input('Enter the divisor: '))

    result = dividend / divisor
    print(f'The result is: {result}')
except ValueError:
    print('Invalid input. Please enter a valid number.')
except ZeroDivisionError:
    print('Cannot divide by zero.')
