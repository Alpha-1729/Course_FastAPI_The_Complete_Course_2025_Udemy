#!/usr/bin/python3
# Dictionary

"""
>>>>
>>>>
>>>>
>>>>
"""

user_dictionary = {"username": "sam", "age": 10, "hobby": "carpenter"}

# Removing a key from the dictionary.
# If key is not in the dictionary, None will be returned.
user_dictionary.pop("username", None)

# OR
del user_dictionary["age"]

# Creating a copy of the dictionary.
dict_copy = user_dictionary.copy()
print(dict_copy)
