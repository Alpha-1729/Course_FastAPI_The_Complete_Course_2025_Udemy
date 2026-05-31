#!/usr/bin/python3
# List Sets And Tuples

"""
>>>> Key Notes:
        - discard() removes an element from a set WITHOUT raising an error if missing.
        - remove() raises a KeyError if the element does not exist.
>>>>
>>>>
>>>>
"""

# List operation.
my_list = [80, 96, 72, 1000]

my_list.pop(2)  # Removes element at index 2 → removes 72
my_list.sort()  # Sorts in ascending order → [80, 96, 1000]

print(my_list)

# Set operation.
my_set = {1, 2, 3, 4, 5}  # Duplicates are ignored in sets

my_set.discard(4)  # Removes 4 → no error if missing
my_set.discard(10)  # 10 doesn't exist → no error (unlike remove())

my_set.clear()  # Empties the set → set()

my_set.update([1, 2, 4])  # Adds multiple elements at once

print(my_set)
