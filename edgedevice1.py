import socket
import paho.mqtt.client as mqtt

HOST = "0.0.0.0"
PORT = 5000 # Make sure socket_sensor.py also uses 5000

broker = "broker.emqx.io"
topic = "savonia/iot/temperature"

# Fix for the DeprecationWarning
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
mqtt_client.connect(broker, 1883)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This line helps reuse the port if the script crashed previously
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

print("Edge device waiting for sensor...")

conn, addr = server.accept()
print("Sensor connected:", addr)

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break

        value = data.decode()
        print("Edge received:", value)

        # Forwarding the data to the cloud
        mqtt_client.publish(topic, value)
        print("Forwarded to MQTT:", value)
except KeyboardInterrupt:
    print("Stopping Edge Device...")
finally:
    conn.close()
    server.close()