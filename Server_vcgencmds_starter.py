import socket
import os
import json

def get_h264_block():
    return os.popen('vcgencmd measure_clock h264').readline().replace("Clock=", "").replace("'C\n", "")

# Function to get the core temperature using vcgencmd
def get_core_temperature():
    return os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", "")

# Function to get the GPU temperature using vcgencmd
def get_gpu_temperature():
    return os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", "")

# Function to get the CPU temperature using the /sys/class/thermal/thermal_zone0/temp file
def get_cpu_temperature():
    try:
        # Read CPU temperature from the file (value is in millidegrees Celsius)
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            temperature = file.readline().strip()
            # Convert millidegrees to degrees Celsius
            return f"{int(temperature) / 1000:.2f}°C"
    except Exception as e:
        return f"Error reading CPU temperature: {str(e)}"

# Function to get the voltage using vcgencmd
def get_voltage():
    return os.popen('vcgencmd measure_volts').readline()

# Function to get the GPU core speed using vcgencmd
def get_gpu_core_speed():
    return os.popen('vcgencmd measure_clock core').readline()

# Function to get the HDMI clock using vcgencmd
def get_hdmi_clock():
    return os.popen('vcgencmd measure_clock hdmi').readline()

# Function to get pixel values (placeholder, replace with actual implementation)
def get_pixel_values():
    return "Pixel Values not implemented yet"

# Function to gather all computer properties
def get_computer_properties():
    core_temp = get_core_temperature()
    gpu_temp = get_gpu_temperature()
    cpu_temp = get_cpu_temperature()
    voltage = get_voltage()
    gpu_core_speed = get_gpu_core_speed()
    hdmi_clock = get_hdmi_clock()
    pixel_values = get_pixel_values()
    h264_block = get_h264_block()

    # Create a dictionary with the property values
    properties_dict = {
        "Core Temperature": core_temp,
        "GPU Temperature": gpu_temp,
        "CPU Temperature": cpu_temp,
        "Voltage": voltage,
        "GPU Core Speed": gpu_core_speed,
        "HDMI Clock": hdmi_clock,
        "Pixel Values": pixel_values,
        "H264 block": h264_block,
        # Add more properties as needed
    }

    return properties_dict

# Set up the socket server
s = socket.socket()
host = ''  # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

while True:
    # Accept incoming connections
    c, addr = s.accept()
    print(f'\nGot connection from {addr}')

    # Retrieve computer properties
    computer_properties = get_computer_properties()

    # Convert dictionary to JSON string
    json_string = json.dumps(computer_properties, indent=2)

    # Convert JSON string to bytes
    res = bytes(json_string, 'utf-8')

    # Send the JSON object to the client
    c.send(res)

    # Close the connection
    c.close()
