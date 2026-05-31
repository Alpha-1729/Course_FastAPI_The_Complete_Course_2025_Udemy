#!/usr/bin/python3
# Dictionary

"""
>>>>
>>>>
>>>>
>>>>
"""

user_info = {"username": "sam", "age": 10, "hobby": "carpenter"}

user_info["married"] = True  # Add a new key
user_info.pop("username", None)  # Remove safely (no error if missing)
del user_info["age"]  # Remove directly (raises error if missing)

copied_dict = user_info.copy()  # Copy before clearing
user_info.clear()  # Empty the dictionary

print(copied_dict)  # {'hobby': 'carpenter', 'married': True}
