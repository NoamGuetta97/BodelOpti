
File Summaries

- **main.py**: Initializes and runs the radar data processing system. It sets up the application, imports modules, and starts the main loop for receiving, processing, and logging radar data.

- **Radar.py**: Defines `RadarSystem` to manage radar-related operations, handling the connection to the radar source, parsing radar messages according to the ICD, and error handling.

- **Other.py**: Provides helper functions to support radar data processing, including handling connections, parsing helper methods, and essential calculations for radar data.

- **Utils.py**: Contains utility functions for data conversion, handling timing, and creating logs. It includes functions like `convert_bytes` and `setup_logging`.

---

# Radar Data Processing System

This repository implements a real-time radar data processing system, designed to manage, process, and log data from radar sources efficiently and reliably. The system is modular, with dedicated components for connection management, data parsing, error handling, and utility functions.

## Features

- **Real-Time Data Processing**: Handles radar data inputs in real-time, parsing and transmitting messages based on defined protocols.
- **Socket-Based Connection**: Connects to radar data sources and central monitoring systems via sockets for continuous data flow.
- **ICD Compliance**: Processes and parses radar data according to the Interface Control Document (ICD) specifications.
- **Error Handling & Logging**: Implements robust error checking, logs critical events, and provides keep-alive messaging to ensure system stability.

## Installation

1. Clone the repository:
   
   git clone https://github.com/NoamGuetta97/macam-RADA
   cd macam-RADA/final changes/
   

2. Install dependencies:
   
   pip install -r requirements.txt
   

## Usage

Start the main processing script:

python main.py


This command initiates the radar data processing loop, continuously receiving, parsing, and logging radar data.

## Project Structure

- **main.py**: Entry point for the radar processing system, initializing modules and starting the main operational loop.
  
- **Radar.py**: Contains the `RadarSystem` class, which manages radar-specific operations, including data parsing, error handling, and socket communication.

- **Other.py**: Helper functions supporting radar operations, including socket connection management, data transformation, and parsing tools.

- **Utils.py**: Utility functions for data conversion, timing, and logging. This module includes functions such as `convert_bytes` for byte data parsing and `setup_logging` for system logging.



## Key Modules and Functions

### main.py
- `main()`: Starts the radar processing application by setting up connections and initializing the radar system.

### Radar.py
- `RadarSystem`: Core class for radar data processing, including methods to parse incoming radar messages, handle errors, and maintain socket connections.

### Other.py
- Various helper functions, including data transformations and socket connection management.

### Utils.py
- `convert_bytes(data)`: Converts raw byte data to structured information.
- `setup_logging()`: Configures logging for monitoring system events and errors.

## Logging

Logs are saved to `radar.log`, detailing important events, errors, and keep-alive messages to aid in debugging and system monitoring.



Acknowledgments

Special thanks to contributors and collaborators involved in the radar data processing and development efforts.

This `README.md` provides an overview of the system, explains its structure, and highlights key features and functions.
