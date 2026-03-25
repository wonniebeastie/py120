def invert_nums(numbers):
    inverse_nums = []
    for num in numbers:
        try:
            inverse_nums.append(1 / num)
        except ZeroDivisionError:
            inverse_nums.append(float('inf'))
    return inverse_nums

print(invert_nums([1, 2, 3, 4, 5])) # [1.0, 0.5, 0.3333333333333333, 0.25, 0.2]
print(invert_nums([0, 1, 2, 3, 4, -5])) # ZeroDivisionError: division by zero
