#!/usr/bin/python3
# List Sets And Tuples

"""
>>>> Remove and Discard method in sets.
        The discard() method removes the specified item from the set.
        This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
>>>>
>>>>
>>>>
"""
# Lists operations.
my_list = [80, 96, 72, 1000]

# Removing an element at a particular position.
my_list.pop(2)  # Remove the element at the index 2.

# Sorting a list.
my_list.sort()

# Set operation.
my_set = {1, 2, 3, 4, 5, 1}

my_set.discard(4)

# This will not raise an error.
my_set.discard(10)

# Removing all elements from sets.
my_set.clear()

# Adding more than one elements.
my_set.update([1, 2, 4])

print(my_set)
