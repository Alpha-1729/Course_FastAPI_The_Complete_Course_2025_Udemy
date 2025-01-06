#!/usr/bin/env python3
# Script to remove rename image files in the directory.

import os
from pathlib import Path

# Change dir to two dir up.
os.chdir(Path(__file__).parents[2])

# List all dir and avoid the .git dir and config folder.
dir_list = list(filter(os.path.isdir, os.listdir()))
dir_list.remove('.git')

for directory in dir_list:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png") and " " in file:
                print(file)
                file_path = os.path.join(root, file)
                new_name = os.path.join(root, file.replace(" ", "_" ))
                os.rename(file_path, new_name)