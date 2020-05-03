# Script used to rename single digit numbers for better sorting

import os

# Get all file list
with os.scandir() as entries:
    # For each file
    for entry in entries:
        # Find first part before underscore
        split_name = entry.name.split("_", 1)
        # If has 4 characters (in dayx_.. format)
        if len(split_name[0]) == 4:
            # Add a zero to convert to day0x_..
            new_name = split_name[0][:3] + "0" + split_name[0][3:] + "_" + split_name[1]
            # Rename
            os.rename(entry.name, new_name)
            # Print new name for check
            print(new_name)
        