import qrcode
import json
import random
import string
from PIL import Image

# Your JSON template
template = {
    "ID": "1",
    "info": "Test.",
    "direction": "Test",
    "home": "Test",
    "opLocation": "Test",
    "freq": "test",
    "lastUpdateTime": "test",
    "vehicleType": "test"
}

template2 = {
    "ID": "1",
    "info": "Test. change2",
    "direction": "Test change1",
    "home": "Test change4",
    "opLocation": "Test change4",
    "freq": "test change4",
    "lastUpdateTime": "test change3",
    "vehicleType": "test"
}

alive_text = "Keep alive!"

# Function to generate random string
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Generate 5 QR codes
for i in range(1):
    # Randomize the template
    for key in template.keys():
        if key != "lastUpdateTime":  # We keep the timestamp constant
            template[key] = generate_random_string(10)  # Generate a random string of length 10

    # Convert the dictionary to a JSON string
    json_str = json.dumps(template)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Use version 40 to get the maximum size
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(template2)
    qr.make(fit=True)

    # Save the QR code as a .png file
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"qr_code_{i}.png")
