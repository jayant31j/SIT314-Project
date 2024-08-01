
# Light Sensing System

## Overview

The Light Sensing System is an innovative project designed to monitor and analyze ambient light levels in various environments. Utilizing an Arduino-based light sensor, the system collects real-time data, which is then processed, stored, and visualized using Python, MongoDB, Plotly, and ThingSpeak. This project aims to provide a comprehensive solution for applications such as smart home automation, agricultural monitoring, and environmental research.

![Light Sensing System](images/light_sensing_system.jpg)

## Features

- **Real-Time Monitoring**: Collects and displays real-time light level data.
- **Data Storage**: Stores collected data in MongoDB for historical analysis.
- **Visualization**: Visualizes data using Plotly for interactive and dynamic graphs.
- **Remote Access**: Sends data to ThingSpeak for remote monitoring.

## Components

- **Microcontroller**: Arduino Uno
- **Sensor**: Light sensor (e.g., LDR, TSL2561)
- **Connectivity**: WiFi module (e.g., ESP8266)
- **Power Supply**: Battery pack

## Setup

### Hardware Setup

1. **Connect the Light Sensor**:
    - Connect the light sensor to the appropriate analog pin on the Arduino.
    - Ensure proper power supply and grounding.

2. **WiFi Module**:
    - Connect the ESP8266 module to the Arduino for WiFi connectivity.

### Software Setup

1. **Arduino IDE**:
    - Install the Arduino IDE from [Arduino's official website](https://www.arduino.cc/en/software).
    - Clone this repository:
      ```sh
      git clone https://github.com/yourusername/light-sensing-system.git
      ```
    - Open `light_sensing_system.ino` in the Arduino IDE.
    - Upload the code to the Arduino board.

2. **Python Environment**:
    - Install Python from [Python's official website](https://www.python.org/downloads/).
    - Install required Python libraries:
      ```sh
      pip install pymongo plotly requests
      ```

3. **MongoDB**:
    - Install MongoDB from [MongoDB's official website](https://www.mongodb.com/try/download/community).
    - Set up a local or cloud-based MongoDB instance.

4. **ThingSpeak**:
    - Create an account on [ThingSpeak](https://thingspeak.com/).
    - Set up a new channel and obtain the API key.
