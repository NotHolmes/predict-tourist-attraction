import os
from PIL import Image
import imagehash

# directory containing the images
place = "wat_phra_chetuphon_(wat_pho)"
image_dir = "../Google-Image-Scraper/photos/" + place + "/"

# dictionary to store hashes of images
hashes = {}

# count the number of images before
num_images_before = len(os.listdir(image_dir))

# create a new directory to store duplicate images
dup_dir = "./" + "duplicate_images/" + place
os.makedirs(dup_dir, exist_ok=True)

# iterate over images in the directory
for filename in os.listdir(image_dir):
    # only process image files
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # open the image and compute its hash
        img_path = os.path.join(image_dir, filename)
        img = Image.open(img_path)
        img = img.convert("RGB")
        hash = str(imagehash.phash(img))
        
        # check if hash already exists
        if hash in hashes:
            # duplicate image found - move it to new directory
            new_path = os.path.join(dup_dir, filename)
            os.rename(img_path, new_path)
            hashes[hash] = new_path
            print(f"Moved duplicate image {img_path} to {new_path}")
        else:
            # new image - store its hash
            hashes[hash] = img_path

# count the number of images after
num_images_after = len(os.listdir(image_dir))

# calculate the number of moved images
num_moved_images = len(os.listdir(dup_dir))

# print the results
print(f"Total number of images before: {num_images_before}")
print(f"Total number of images after: {num_images_after}")
print(f"Number of moved images: {num_moved_images}")