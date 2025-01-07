import serial
import webbrowser
import re  # Regular expression for data validation

# Set up serial connection
arduino = serial.Serial('COM8', 9600, timeout=1)

# Define valid RFID tags and associated websites
valid_rfid_tags = {
    "131c27da": "https://www.youtube.com/@JS.MAKERS/videos",
    "ee6b332": "https://github.com/JSMAKERS015/open-website-usin-RFID",
}

print("Waiting for RFID scan...")

while True:
    if arduino.in_waiting > 0:
        # Read the serial data
        raw_data = arduino.readline().decode('utf-8', errors='ignore').strip()
        print(f"Raw RFID Data: {raw_data}")

        # Validate data to allow only hexadecimal characters
        match = re.match(r'^[0-9a-fA-F]+$', raw_data)
        if match:
            rfid_data = match.group(0)
            print(f"Validated RFID Data: {rfid_data}")
            
            # Check if the RFID tag is valid
            if rfid_data in valid_rfid_tags:
                print(f"Opening website: {valid_rfid_tags[rfid_data]}")
                webbrowser.open(valid_rfid_tags[rfid_data])
            else:
                print("Invalid RFID tag.")
        else:
            print("Invalid RFID data format.")
