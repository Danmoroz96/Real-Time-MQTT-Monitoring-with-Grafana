# Real-Time-MQTT-Monitoring-with-Grafana
In this lab, I extended the IoT pipeline by adding a real-time monitoring dashboard.


This project demonstrates a complete IoT data pipeline involving Socket Programming, Edge Computing, and Cloud Visualization using Grafana.

1. System Overview
The system consists of two physical nodes (in my case I used one for both nodes) simulating a real-world industrial IoT environment where a sensor sends data to a gateway, which then pushes it to the cloud.

Laptop 1 (program 1) (Sensor): Generates simulated data (e.g., temperature) and sends it over a TCP socket.

Laptop 2 (Edge Device): Acts as a gateway. It listens for socket data, processes it, and publishes it to an MQTT Broker.

Laptop 1 (Main Server): Subscribes to the MQTT Broker and visualizes the incoming data stream in a real-time Grafana Dashboard.

2. Data Flow & Configuration
Socket Communication

Source: socket_sensor.py (Laptop 1)

Destination: edge_device.py (Laptop 2)

Protocol: TCP Socket

Port: [INSERT YOUR PORT, e.g., 5000]

MQTT Configuration

Broker: broker.emqx.io

Port: 1883

Topic: [INSERT YOUR TOPIC, e.g., savonia/iot/temperature]

3. Grafana Setup
To visualize the data, Grafana was configured on Laptop 1 as follows:

Installation: Installed via the Windows standalone binary.

Plugin: Added the MQTT Data Source via the Connections menu.

Connection: Configured the data source to point to broker.emqx.io:1883.

Dashboard: Created a new panel using the MQTT data source, subscribing to the topic [INSERT YOUR TOPIC].

4. Limitations
Important Note on Data Persistence: This setup is designed for live monitoring only. The Grafana MQTT data source visualizes messages as they arrive in the browser. It does not store historical data. If the dashboard is refreshed or the connection is lost, previous data points disappear. For long-term trends, a time-series database like InfluxDB or Prometheus would be required.

The dashboard was configured using the Grafana MQTT Data Source plugin.

Panel Type: [e.g., Gauge or Time Series]

What is shown: The panel displays the real-time value of the sensor data received via the MQTT topic. As the value changes in socket_sensor.py, the gauge/graph updates immediately on the screen.


5. Limitation: Live-Only Visualization
This implementation uses the MQTT Data Source, which is designed for live monitoring only.

Limitation: Grafana does not store the data in a database in this specific setup.

Impact: If the browser is refreshed or the dashboard is closed, all previous data points are lost. For historical data, a time-series database (like InfluxDB) would need to be added to the pipeline.

Reflection Questions
1. What is the role of Grafana in this system?
Grafana serves as the Presentation Layer. It abstracts the technical complexity of MQTT packets and turns them into a user-friendly visual interface, allowing operators to monitor sensor health without reading raw terminal logs.

2. Why is MQTT useful for monitoring applications?
MQTT is a lightweight, "publish/subscribe" protocol designed for low-bandwidth, unreliable networks. It is useful because it decouples the data producer (Edge Device) from the consumer (Grafana), allowing multiple devices to monitor the same data stream efficiently.

3. What is the difference between live monitoring and historical storage?

Live Monitoring: Provides immediate visibility into the current state of a system (the "now").

Historical Storage: Involves saving data to a database to analyze patterns, perform audits, or predict future failures based on past behavior.

6. How to Run
On Laptop 2: Run python edge_device.py. (I used edgedevice1.py)

On Laptop 1: Run python socket_sensor.py. ( I used socket_sensor1.py)

On Laptop 1: Log into http://localhost:3000 to view the live dashboard.

Screenshots of the program:

![Screenshot 2026-03-25 133025](https://github.com/user-attachments/assets/6fb17efc-f5a6-4198-8c46-9daf27ae05c8)

![Screenshot 2026-03-25 133242](https://github.com/user-attachments/assets/84d206bf-7a17-48fe-8b44-7ebd88e17e07)

![Screenshot 2026-03-25 133358](https://github.com/user-attachments/assets/53a107cf-4709-4f89-9c23-4430bf3acc4e)



