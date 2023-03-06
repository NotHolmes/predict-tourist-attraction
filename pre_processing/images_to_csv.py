import os
import numpy as np
import pandas as pd
from PIL import Image

# Set the path to the directory containing the subdirectories
data_dir = './dataset/data/'

# Get the list of subdirectories (which are the labels)
labels = sorted(os.listdir(data_dir))

# Define the size of the images
img_size = (32, 32)

# Initialize the data and label arrays
data = np.zeros((0, img_size[0]*img_size[1]*3), dtype=np.uint8)
labels_data = np.zeros((0,), dtype=np.int32)

# Loop through the subdirectories and load the images
for label_idx, label in enumerate(labels):
    label_dir = os.path.join(data_dir, label)
    file_names = os.listdir(label_dir)
    for file_name in file_names:
        file_path = os.path.join(label_dir, file_name)
        with Image.open(file_path) as img:
            # Resize the image to the desired size and flatten it
            img = img.resize(img_size)
            img_flat = np.array(img).flatten()
            # Check that the flattened image has the expected size
            if img_flat.shape[0] != img_size[0]*img_size[1]*3:
                continue
            # Append the image and label to the data and label arrays
            data = np.vstack((data, img_flat))
            labels_data = np.append(labels_data, label_idx)

# Convert the data and label arrays to dataframes
df_data = pd.DataFrame(data)
df_labels = pd.DataFrame(labels_data, columns=['label'])

# Concatenate the data and label dataframes and save to a CSV file
df = pd.concat([df_data, df_labels], axis=1)
df.to_csv('./dataset/dataset32.csv', index=False)
