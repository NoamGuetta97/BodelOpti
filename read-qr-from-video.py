import os
import cv2
import json
import pyzbar.pyzbar as pyzbar

# Define a function to decode QR codes from a video frame


def decode_qr(frame):
    # Decode the QR codes in the frame
    decoded_objects = pyzbar.decode(frame)

    # Return the decoded data
    return [json.loads(obj.data.decode("utf-8")) for obj in decoded_objects if obj.data.decode("utf-8").startswith('{')]

# Define a function to write JSON data to a log file


def write_to_log(data, log_file, read_number):
    with open(log_file, "a") as f:
        # Write the read number to the file
        f.write(f"Read number {read_number}:\n")

        # Write the data to the file in a pretty, indented format
        f.write(json.dumps(data, indent=4))
        f.write("\n")


# Define the log file
log_file = "log.txt"

# Delete the old log file if it exists
if os.path.exists(log_file):
    os.remove(log_file)

# Initialize the read number
read_number = 1

# Initialize the last ID
last_id = None

# Open the default camera
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was read successfully
    if ret:
        # Decode the QR codes in the frame
        data = decode_qr(frame)

        # Write the decoded data to the log file
        for item in data:
            # If the ID is different from the last ID
            if item.get("ID") != last_id:
                write_to_log(item, log_file, read_number)
                read_number += 1

                # Update the last ID
                last_id = item.get("ID")
    else:
        break

# Release the camera
cap.release()

print(
    f"The QR codes from the video feed have been successfully decoded and written to the {log_file} file.")
