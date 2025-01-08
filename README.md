
# **WEBSITE Opening Uising RFID** 

Using this code you can open any favourite website using the RFID Module.

### **STEPS:**

1. First you have to get your RFID Card Unique ID. The code to scan your card's unique ID is below:

```
import serial
import webbrowser
import re  # Regular expression for data validation

# Set up serial connection
arduino = serial.Serial('COM8', 9600, timeout=1)

# Define valid RFID tags and associated websites
valid_rfid_tags = {
    "131c27da": "https://www.youtube.com/@JS.MAKERS/videos",
    "ee6b332": "https://www.youtube.com/shorts/ZsnUpIGjvKg",
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
```



2.  After Uploading the code open the serial monitor and scan your card. Below you can find your Unique ID copy and store the ID somewhere safe.
   
![Capture](https://github.com/user-attachments/assets/8a6d7776-2bd6-42d1-8397-ff872440694e)



3. Next, open the VS Code Application to run the Python code to open a website using RFID.

4. Create a new folder and open it as Project.

5. Inside the folder create a new file with .py extension.

6. Paste the code which I provided.

  ```
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
```


7. Replace the Unique ID with your card ID and replace the website with your particular website. 


![2](https://github.com/user-attachments/assets/5d6ef827-1fa3-4999-9736-02cd8c069827)



8. Before running the code you have to install some scripts:

- Install the pyserial package: Open a terminal or command prompt and run:

```
pip install pyserial
```

- Verify the Installation: After installation, verify that the package is installed by running:

```
pip show pyserial
```

This should display details about the installed pyserial package.

11. After installing the scrips run the program. You will get a scan card message on your terminal, as shown below:
    
![3](https://github.com/user-attachments/assets/b9f59dc2-2c32-45f6-8b84-3852206769bb)



