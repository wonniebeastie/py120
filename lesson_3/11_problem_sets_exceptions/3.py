try:
    dividend = float(input('Enter the dividend: '))
    divisor = float(input('Enter the divisor: '))

    result = dividend / divisor
except (ValueError, ZeroDivisionError):
    print('Got ValueError or ZeroDivisionError')
else:
    print(f'The result is: {result}')
finally:
    print('End of the program.')
