#install library: pip install paho-mqtt
import paho.mqtt.client as mqtt

import json

# Configuration
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "marvelmind"

# Callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC) # Subscribe upon connection

def on_message(client, userdata, msg):
    input_data= json.loads(msg.payload.decode())
    input_data_tree= json.dumps(input_data, cls=json.JSONEncoder, indent=2)
    print(f"Received: {input_data_tree} on {msg.topic}") # Process messages
    #print(f"Received: {msg.payload.decode()} on {msg.topic}") # Process messages

# Setup and run client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60) # Connect to broker
client.loop_forever() # Network loop