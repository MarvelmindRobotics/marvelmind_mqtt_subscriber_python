# marvelmind_mqtt_subscriber_python
Example of Marvelmind MQTT subscriber (Python)

This is an exampler of MQTT subscriber to receive data published 
by Marvelmind dashboard or another components of the system. 

To use this subscriber:
- Achieve a good tracking using the Marvelmind navigation system.
  Refer to operating manual (https://marvelmind.com/pics/marvelmind_navigation_system_manual.pdf)
  and other documents on https://marvelmind.com for details.
- Install MQTT library for python: pip install paho-mqtt
- Run the subsctiber from console: 
  "python ./mm_mqtt_example.py" or "python3 ./mm_mqtt_example.py"
- In Marvelmind dashboard select menu "Settings/MQTT settings"
-   In the window select checkbox "MQTT output enable"
-   Keep default destination settings:
    "Destination server" - test.mosquitto.org
    "Port" - 1883
    "Topic folder" - marvelmind
- Select required data to transmit by corresponding checkboxes (mobile beacon location, telemetry, IMU etc)
- Data in JSON format should come to the python application via selected MQTT broker (test.mosquitto.org).
  See MQTT chapter in interfaces document (https://marvelmind.com/pics/marvelmind_interfaces.pdf) for more details.
- This example prints incoming data to the console.



