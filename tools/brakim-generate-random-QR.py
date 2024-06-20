import qrcode
import json
import random

# Function to generate random float
def random_float():
    return round(random.uniform(-180.0, 180.0), 6)

# Function to generate random uint
def random_uint():
    return random.randint(1, 1000)

# Function to generate random bool
def random_bool():
    return bool(random.getrandbits(1))

# Function to generate random str
def random_str():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    

# # # Generate 10 QR codes
# for i in range(10):
#     # JSON data with random values
#     data = {
#     "c": {
#         "i": random_uint(),
#         "n": random_uint(),
#         "p": random_uint(),
#     },
#     "s": {
#         "s": random_uint(),
#         "o": {
#             "l": random_float(),
#             "l": random_float(),
#         }
#     },
#     "p": [
#         {
#             "t": random_uint(),
#             "c": [
#                 {
#                     "l": random_float(),
#                     "l": random_float(),
#                 }
#             ]
#         }
#     ],
#     "d": [
#         {
#             "i": random_str(),
#             "t": random_uint(),
#             "l": {
#                 "l": random_float(),
#                 "l": random_float(),
#                 "a": random_float(),
#                 "t": random_uint(),
#             },
#             "h": {
#                 "l": random_float(),
#                 "l": random_float(),
#                 "a": random_float(),
#                 "t": random_uint(),
#             },
#             "o": {
#                 "l": random_float(),
#                 "l": random_float(),
#                 "a": random_float(),
#                 "t": random_uint(),
#             },
#             "v": {
#                 "x": random_float(),
#                 "y": random_float(),
#                 "z": random_float(),
#             },
#             "d": random.choice(["Radar", "Skylock", "Niso"]),
#             "s": random_uint(),
#             "f": random.choice(["ENEMY", "FRIENDLY", "UNKNOWN"]),
#             "a": random_bool(),
#             "m": random_str(),
#             "f": random_str(),
#             "t": random_str(),
#             "a": random_float(),
#         }
#     ]
# }

# # Generate 10 QR codes
for i in range(1):
    # JSON data with random values
    data = {
    "chunk": {
        "id": random_uint(),
        "num_parts": random_uint(),
        "part_idx": random_uint(),
    },
    "system": {
        "system_id": random_uint(),
        "operator_pos": {
            "lat": random_float(),
            "lng": random_float()
        }
    },
    "polygons": [
        {
            "type": random_uint(),
            "coordinates": [
                {
                    "lat": random_float(),
                    "lng": random_float()
                }
            ]
        }
    ],
    "detections": [
        {
            "id": random_str(),
            "time": random_uint(),
            "last_pos": {
                "lat": random_float(),
                "lng": random_float(),
                "alt": random_float(),
                "time": random_uint()
            },
            "home_pos": {
                "lat": random_float(),
                "lng": random_float(),
                "alt": random_float(),
                "time": random_uint()
            },
            "operator_pos": {
                "lat": random_float(),
                "lng": random_float(),
                "alt": random_float(),
                "time": random_uint()
            },
            "velocity": {
                "x": random_float(),
                "y": random_float(),
                "z": random_float()
            },
            "detected_by": random.choice(["Radar", "Skylock", "Niso"]),
            "seconds_to_impact": random_uint(),
            "friendly_status": random.choice(["ENEMY", "FRIENDLY", "UNKNOWN"]),
            "active": random_bool(),
            "model": random_str(),
            "frequency": random_str(),
            "track_type": random_str(),
            "azimuth": random_float()
        }
    ]
}


    # Convert the data to string
    data_str = json.dumps(data)

    # Create QR code instance
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to QR code
    qr.add_data(data)

    #print(data_str)

    # Make the data into a QR code
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(f'QR/qrcode_{i}.png')
    break
