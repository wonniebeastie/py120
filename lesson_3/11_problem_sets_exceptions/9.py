numbers = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5, 6]

# LBYL approach
"""
Check for potential errors before executing code that might fail.
"""
"""
I: a list of numbers
O: int, sixth element or `None` if none found

- if length of list is less than 6:
    - return `None`
- return element
"""
def get_sixth_elem_lbyl(num_list):
    if len(num_list) < 6:
        return None
    return num_list[5]

print(get_sixth_elem_lbyl(numbers)) # None
print(get_sixth_elem_lbyl(nums)) # 6
