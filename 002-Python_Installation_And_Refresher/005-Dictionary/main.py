#!/usr/bin/python3
# Dictionary

"""
>>>>
>>>>
>>>>
>>>>
"""

user_info = {"username": "sam", "age": 10, "hobby": "carpenter"}

# Remove a key safely, returning None if it doesn't exist
user_info.pop("username", None)

# Alternative way to remove a key
del user_info["age"]

# Create a copy of the dictionary
copied_dict = user_info.copy()
print(copied_dict)

