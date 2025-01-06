#!/usr/bin/python3
# Script to create a template.

import os
import json
import shutil
from pathlib import Path

# Change dir to two directories up.
os.chdir(Path(__file__).parents[2])

config_json_path = os.path.join(os.getcwd(), "config", "settings.json")

# Read the config from the config.json file.
with open(config_json_path, "r") as config_file:
    config_data = json.load(config_file)

latest_section = config_data["section"]["latest"]

pre_run_command = config_data["template"]["pre-run-command"]

template_prefix = config_data["template"]["prefix"]
template_prefix = f"-{template_prefix}" if len(template_prefix.strip()) > 0 else ""

template_number = config_data["template"]["number"]

template_name = input("Enter Template Name: ")
template_name = [word.capitalize() for word in template_name.split(" ")]
template_name = "_".join(template_name)

topic_name = template_name.replace("_", " ")

template_dir_name = "{}{}-{}".format(
    str(template_number).zfill(3), template_prefix, template_name
)
destination_path = os.path.join(os.getcwd(), latest_section, template_dir_name)

# Determine the template path: Use section-specific template if it exists, otherwise use the default.
section_template_path = os.path.join(os.getcwd(), latest_section, "templates")
default_template_path = os.path.join(os.getcwd(), "config", "templates")
template_path = section_template_path if os.path.exists(section_template_path) else default_template_path

# Moving all the content from the selected template folder to the destination.
shutil.copytree(template_path, destination_path)

# Looping through destination directory and replacing placeholders in scripts.
for root_dir, sub_dir, file_list in os.walk(destination_path):
    if file_list:
        for file in file_list:
            full_file_path = os.path.join(root_dir, file)

            # Read the content in the file and replace placeholders.
            with open(full_file_path, errors="ignore") as in_file:
                file_content = in_file.read()

            file_content = file_content.replace("<topic>", topic_name)

            with open(full_file_path, "w") as out_file:
                out_file.write(file_content)

# Update the template info in the config file.
config_data["template"]["number"] += 1
config_data["template"]["section"] = config_data["section"]["latest"]
config_data["template"]["latest"] = template_dir_name
with open(config_json_path, "w") as config_file:
    json.dump(config_data, config_file, indent=4)

# Executing pre-run command.
if os.path.exists(destination_path) and pre_run_command:
    os.chdir(destination_path)
    os.system(pre_run_command)
