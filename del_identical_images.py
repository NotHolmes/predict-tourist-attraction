import os
from PIL import Image
import imagehash

# directory containing the images
image_dir = "./The_Grand_Palace_Bangkok"

# dictionary to store hashes of images
hashes = {}

# count the number of images before
num_images_before = len(os.listdir(image_dir))

# iterate over images in the directory
for filename in os.listdir(image_dir):
    # only process image files
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # open the image and compute its hash
        img_path = os.path.join(image_dir, filename)
        img = Image.open(img_path)
        img = img.convert("RGBA")
        hash = str(imagehash.phash(img))
        
        # check if hash already exists
        if hash in hashes:
            # duplicate image found - delete it
            os.remove(img_path)
            print(f"Deleted duplicate image {img_path}")
        else:
            # new image - store its hash
            hashes[hash] = img_path

# count the number of images after
num_images_after = len(os.listdir(image_dir))

# calculate the number of deleted images
num_deleted_images = num_images_before - num_images_after

# print the results
print(f"Total number of images before: {num_images_before}")
print(f"Total number of images after: {num_images_after}")
print(f"Number of deleted images: {num_deleted_images}")
