import os
import json
import cv2
import pyzbar.pyzbar as pyzbar
import time

# Define a function to decode QR codes from an image


def decode_qr(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Decode the QR codes in the image
    decoded_objects = pyzbar.decode(img)

    # Return the decoded data
    return [json.loads(obj.data.decode("utf-8")) for obj in decoded_objects]

# Define a function to write JSON data to a log file


def write_to_log(data, log_file, read_number):
    with open(log_file, "a") as f:
        # Write the read number to the file
        f.write(f"Read number {read_number}:\n")

        # Write the data to the file in a pretty, indented format
        f.write(json.dumps(data, indent=4))
        f.write("\n")

# Define a function to print the time in minutes and seconds


def print_execution_time(start_time):
    end_time = time.time()
    execution_time = end_time - start_time
    minutes = int(execution_time // 60)
    seconds = int(execution_time % 60)
    print(f"Execution time: {minutes} minutes {seconds} seconds")


# Define the folder containing the QR code images
folder = "QR"

# Define the log file
log_file = "pic-log.txt"

# Delete the old log file if it exists
if os.path.exists(log_file):
    os.remove(log_file)

# Initialize the read number
read_number = 1

# Record the start time
start_time = time.time()

# Iterate over the images in the folder
for filename in os.listdir(folder):
    # If the file is an image
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Decode the QR codes in the image
        data = decode_qr(os.path.join(folder, filename))

        # Write the decoded data to the log file
        for item in data:
            write_to_log(item, log_file, read_number)
            read_number += 1

# Print the execution time
print_execution_time(start_time)

print(
    f"The QR codes from the images in the {folder} folder have been successfully decoded and written to the {log_file} file.")
