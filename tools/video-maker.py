import cv2
import os
from PIL import Image
import numpy as np
import random

# Directory containing the images
dir_path = "QR"
# The image that is not in the 'QR' folder
other_image_path = "alive.png"

# Load the other image without resizing to avoid distortion
other_image = Image.open(other_image_path)

# Get a list of all the image files in the directory
image_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# Sort the images by name 
image_files.sort()

# Desired size (Full HD)
new_size = (1920, 1080)

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('output.mp4', fourcc, 1/3, new_size)

# Create a white background image for the frames
background_image = Image.new('RGB', new_size, (255, 255, 255))

for image_file in image_files:
    # Open an image from 'QR' folder 
    img1 = Image.open(os.path.join(dir_path, image_file))

    # Generate a random number
    rand_num = random.randint(1, 4)

    if rand_num == 1:
        # Add a frame with only the other image
        frame = background_image.copy()
        frame.paste(im=other_image.resize((new_size[0]//2, new_size[1])), box=(0, 0))
    elif rand_num == 2:
        # Add a frame with only the image from the 'QR' folder
        frame = background_image.copy()
        frame.paste(im=img1.resize((new_size[0]//2, new_size[1])), box=(0, 0))
    elif rand_num == 3:
        # Add a frame with both images side by side
        combined_image = Image.new('RGB', new_size, (255, 255, 255))
        combined_image.paste(im=other_image.resize((new_size[0]//2, new_size[1])), box=(0, 0))
        combined_image.paste(im=img1.resize((new_size[0]//2, new_size[1])), box=(new_size[0]//2 , 0))
        frame = combined_image
    else:
        # Add a blank (white) frame
        frame = background_image.copy()

    # Check if frame is an image
    if isinstance(frame, Image.Image):
        # Convert the PIL Image to a numpy array and then to a uint8 data type
        frame = np.array(frame).astype(np.uint8)
        # Write the frame to the video
        video.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    else:
        print(f"Skipping frame for file {image_file} due to invalid frame data.")

video.release()
