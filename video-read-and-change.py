import os
import cv2
import json
import pyzbar.pyzbar as pyzbar
import time

# Define a function to decode QR codes from a video frame
def decode_qr(frame):
    # Decode the QR codes in the frame
    decoded_objects = pyzbar.decode(frame)

    # Initialize an empty list to store valid JSON data
    decoded_data = []

    # Iterate through each decoded object
    for obj in decoded_objects:
        try:
            # Attempt to decode the object's data as JSON
            json_data = json.loads(obj.data.decode("utf-8"))
            # Check if the decoded JSON data is a dictionary
            if isinstance(json_data, dict):
                # Append the decoded data to the list
                decoded_data.append(json_data)
        except json.decoder.JSONDecodeError:
            # Skip over the object if decoding as JSON fails
            pass

    return decoded_data

# Define a function to read data from the log file
def read_log_data(log_file):
    data = []
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            lines = f.readlines()
            current_entry = {}
            for line in lines:
                if line.startswith("Read number"):
                    if current_entry:
                        data.append(current_entry)
                    current_entry = {}
                elif line.strip() and current_entry:
                    current_entry.update(json.loads(line.strip()))
    return data

# Define a function to write JSON data to a log file
def write_to_log(data, log_file, read_number, timestamp, changed_params=None):
    with open(log_file, "a") as f:
        # Write the read number to the file
        f.write(f"Read number {read_number} (Timestamp: {timestamp:.4f}):")
        
        # If parameters changed, mention them
        if changed_params:
            f.write(" (parameters changed: ")
            f.write(", ".join(changed_params))
            f.write(")")

        f.write("\n")

        # Write the data to the file in a pretty, indented format
        f.write(json.dumps(data, indent=4))
        f.write("\n")

# Define the log file
log_file = "vid-log.txt"

# Create an empty log file if it doesn't exist
if not os.path.exists(log_file):
    open(log_file, 'w').close()

# Initialize the read number
read_number = 1

# Open the default camera
cap = cv2.VideoCapture(1)

while (cap.isOpened()):
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was read successfully
    if ret:
        # Record the start time
        start_time = time.time()

        # Decode the QR codes in the frame
        data = decode_qr(frame)

        # Calculate the time taken to decode
        end_time = time.time()
        
        # Read existing log data
        existing_log_data = read_log_data(log_file)

        # Check each QR code data
        for item in data:
            found_in_log = False
            for log_entry in existing_log_data:
                # Check if the ID exists in the log
                if item["ID"] == log_entry.get("ID"):
                    found_in_log = True
                    changed_params = []
                    for key, value in item.items():
                        if key in log_entry and log_entry[key] != value:
                            changed_params.append(key)
                    if changed_params:
                        write_to_log(item, log_file, read_number, end_time, changed_params)
                        read_number += 1
                        print(f"Data for ID {item['ID']} has changed in parameters: {', '.join(changed_params)}.")

            if not found_in_log:
                # If not found in log, add the new data
                write_to_log(item, log_file, read_number, end_time)
                read_number += 1

    else:
        break

# Release the camera
cap.release()

print(
    f"The QR codes from the video feed have been successfully decoded and written to the {log_file} file.")
