import os
import shutil
from PIL import Image
import imagehash

# define the directory to search for duplicate images
directory_to_search = './dataset/data/'

# define the directory to move duplicate images to
duplicated_dir = './duplicated/'

# create the duplicated directory if it doesn't exist
if not os.path.exists(duplicated_dir):
    os.mkdir(duplicated_dir)

# loop through each directory in the specified directory
for subdir, dirs, files in os.walk(directory_to_search):
    # create a hash table to keep track of hashes and paths
    hash_table = {}
    # count the number of files before processing
    file_count_before = len(files)
    
    # loop through each file in the directory
    for file in files:
        # only consider image files
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('webp'):
            # open the image file, convert it to RGB mode, and compute its hash
            with Image.open(os.path.join(subdir, file)).convert('RGB') as img:
                hash_val = str(imagehash.phash(img))
            
            # if the hash already exists, move the file to the duplicated directory
            if hash_val in hash_table:
                source_path = os.path.join(subdir, file)
                dest_dir = os.path.join(duplicated_dir, hash_table[hash_val])
                
                # create the destination directory if it doesn't exist
                if not os.path.exists(dest_dir):
                    os.mkdir(dest_dir)
                
                # move the file to the duplicated directory
                shutil.move(source_path, os.path.join(dest_dir, file))
            
            # otherwise, add the hash and path to the hash table
            else:
                hash_table[hash_val] = os.path.basename(subdir)
    
    # count the number of files after processing
    file_count_after = len([f for f in os.listdir(subdir) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')])
    
    # print the file counts for the directory
    print(f"{subdir}: {file_count_before} files before, {file_count_after} files after")