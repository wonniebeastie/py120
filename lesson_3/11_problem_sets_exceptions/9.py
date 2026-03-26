numbers = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5, 6]

# LBYL approach
"""
Check for potential errors before executing code that might fail.
"""
def get_sixth_elem_lbyl(num_list):
    if len(num_list) < 6:
        return None
    return num_list[5]

print(get_sixth_elem_lbyl(numbers)) # None
print(get_sixth_elem_lbyl(nums)) # 6

# AFNP approach
"""
Try it out & handle errors that can arise.
"""
def get_sixth_elem_afnp(num_list):
    try:
        return num_list[5]
    except IndexError:
        return None

print(get_sixth_elem_afnp(numbers)) # None
print(get_sixth_elem_afnp(nums)) # 6
