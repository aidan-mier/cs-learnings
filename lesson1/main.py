""" Part 1: Comments """
# This is a single line comment

"""
This is a 
multiline comment
"""

""" Part 2: Data types in python """
_bool = True or False
_string = "hello"
_int = 1
_float = 1.42
_float1 = 1e-3
_lst = ["lol", "Pop", 100] #This is a list
_tup = (1, 2) #This is a tuple
_dct = {
        "hello" : "world",
        100 : "One Hundred"
    }
_set = set([1,2,3,4]) #Sets help to show what you have written once and not print repeats.

""" Part 3: Type casting & Checking """
# Cast a float to an int
_cast_to_int = int(_float)
print(f"Cast float to int {_cast_to_int}")

_cast_to_float = float(_int)
print(f"Cast int to float {_cast_to_float}")

_cast_int_to_string = str(_int)
print(f"Cast int to str {_cast_int_to_string}")

print(f"Type for _cast_to_int: {type(_cast_to_int)}")
print(f"Type for _cast_int_to_string: {type(_cast_int_to_string)}")
print(f"Is _cast_int_to_string a string? : {type(_cast_int_to_string) == str}")

""" Part 4: Ceil & floor functions using the math library """
import math
print(math.ceil(_float))

# Shorter way to call the functions
from math import floor, ceil
print(floor(_float))
print(ceil(_float))

# Change the reference name of the library
import math as mth
print(mth.ceil(_float))

""" Part 5: Additions / multiplications """
print(f"Int + Float: {_int + _float}")
print("Hello " + "world")
print("Hello " * 3)

""" Part 6: List comprehension """
_lst_cmp = ["asd" for xx in range(10) if xx % 2 == 0]
print(_lst_cmp)

_lst_cmp = []
for xx in range(10):
    if xx % 2 == 0:
        _lst_cmp.append(xx ** 2)
print(_lst_cmp)