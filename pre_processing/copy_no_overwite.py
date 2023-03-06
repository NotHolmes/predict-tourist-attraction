import os
import shutil
from datetime import datetime

root_dir = './pre_processing/new/test/'
backup_dir = './pre_processing/new/testtest/'

# create the backup directory if it doesn't exist
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

# loop through each subdirectory and file in the root directory
for dir_path, _, file_names in os.walk(root_dir):
    for file_name in file_names:
        # only consider image files
        if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg') or file_name.endswith('.webp'):
            # get the file name and extension
            name, extension = os.path.splitext(file_name)
            # add a suffix number to the file name if it already exists
            suffix = 1
            new_name = f"{name}_{suffix}{extension}"
            dest_dir = os.path.join(backup_dir, os.path.relpath(dir_path, root_dir))
            dest_path = os.path.join(dest_dir, new_name)
            while os.path.exists(dest_path):
                suffix += 1
                new_name = f"{name}_{suffix}{extension}"
                dest_path = os.path.join(dest_dir, new_name)
            # create the destination directory if it doesn't exist
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # copy the file to the destination directory
            shutil.copy2(os.path.join(dir_path, file_name), dest_path)
