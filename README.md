---

# QR Code Data Transfer System

This project enables data transfer between two computers on completely different networks using QR codes. One system encodes data into QR codes for display, while this system captures, decodes, parses, and validates the data using a camera.

## Project Overview

This system reads data from QR codes displayed on a screen and parsed via a connected camera. It's designed for environments with network constraints, allowing data exchange through optical means.

## Features

- **QR Code Scanning**: Reads QR codes displayed on the paired system.
- **Data Parsing**: Decodes and parses the data from the QR codes.
- **Validation**: Ensures the integrity of received data.
- **Seamless Data Transfer**: Enables data exchange between isolated networks.

## Prerequisites

- **Hardware**: Camera positioned to read QR codes from the display.
- **Python 3.8+**
- **Dependencies**: Listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/NoamGuetta97/BodelOpti
   cd qr-data-transfer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Position the camera to accurately read the QR codes.

## Usage

1. Run the program with the command:
   ```bash
   python readAndChange.py
   ```

2. Ensure that the camera is capturing the QR codes correctly. The parsed data will be displayed as output in the terminal.

3. Adjust the camera angle and lighting as needed to improve QR code readability.

## File Overview

- **`readAndChange.py`**: Main script to initialize QR code reading and handle data parsing.
- **`validate.py`**: Module for validating QR code data to ensure accuracy and integrity.
- **`reader.py`**: Manages QR code scanning and decoding from the camera feed.

## Output

The output of this project is the decoded and validated data from the QR codes, displayed in the terminal.

## Troubleshooting

- **Camera Angle**: Ensure the camera is directly facing the screen to capture the QR codes without distortion.
- **Lighting**: Adequate lighting improves QR code readability.
- **Dependencies**: Confirm that all dependencies are correctly installed.

---
