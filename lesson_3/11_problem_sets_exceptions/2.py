try:
    dividend = float(input('Enter the dividend: '))
    divisor = float(input('Enter the divisor: '))

    result = dividend / divisor
except ValueError:
    print('Invalid input. Please enter a valid number.')
except ZeroDivisionError:
    print('Cannot divide by zero.')
else:
    print(f'The result is: {result}')
finally:
    print('End of the program.')
