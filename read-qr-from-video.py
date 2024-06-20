import os
import cv2
import json
import pyzbar.pyzbar as pyzbar

# Define a function to decode QR codes from a video frame
def decode_qr(frame):
    decoded_objects = pyzbar.decode(frame)
    decoded_data = []
    for obj in decoded_objects:
        qr_data = obj.data.decode("utf-8")
        decoded_data.append(qr_data)
    return decoded_data

# Define a function to write data to a log file in JSON format
def write_to_log(data, log_file):
    try:
        # Convert the string representation of a dictionary to a JSON string
        json_data_str = data.replace("'", "\"").replace("None", "null")
        json_data = json.loads(json_data_str)
        transformed_data = transform_data(json_data)
        with open(log_file, "a") as f:
            json.dump(transformed_data, f, indent=4)
            f.write("\n")
        print(f"Data written to log: {transformed_data}")  # Debugging print
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {data}")
    except (TypeError, KeyError) as e:
        print(f"Error processing data: {e}")

# Function to transform the data to the new format
def transform_data(data):
    if not isinstance(data, dict):
        raise TypeError("Data is not a dictionary")

    if "p" in data:
        transformed_polygons = [
            {
                "type": poly["t"],
                "coordinates": [
                    {"lat": coord["lat"], "lng": coord["lng"]}
                    for coord in coords
                ] 
            }
            for poly in data["p"] for coords in poly["co"]
        ]
    else:
        transformed_polygons = []

    return {
        "chunk": {
            "id": data["c"]["id"],
            "num_parts": data["c"]["np"],
            "part_idx": data["c"]["idx"]
        },
        "system": {
            "system_id": data["s"]["id"],
            "operator_pos": {
                "lat": data["s"]["op"]["lat"],
                "lng": data["s"]["op"]["lng"]
            }
        },
        "polygons": transformed_polygons,
        "detections": data.get("d", [])
    }

# Define the log file
log_file = "vid-log2.json"

# Delete the old log file if it exists
if os.path.exists(log_file):
    os.remove(log_file)
    print(f"Deleted old log file: {log_file}")

# Set to keep track of already processed QR codes
processed_qr_codes = set()

# Open the default camera
cap = cv2.VideoCapture(1)  # Changed to 0 to use the default camera

if not cap.isOpened():
    print("Error: Could not open video capture.")
else:
    print("Video capture opened successfully.")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        decoded_qr_data = decode_qr(frame)

        for qr_data in decoded_qr_data:
            if qr_data not in processed_qr_codes:
                print(f"Decoded QR data: {qr_data}")  # Print the QR data for debugging
                write_to_log(qr_data, log_file)
                processed_qr_codes.add(qr_data)
    else:
        print("Error: Could not read frame.")
        break

cap.release()

