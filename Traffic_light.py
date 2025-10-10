import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt

topics = {
    "N": "traffic/N",
    "S": "traffic/S",
    "E": "traffic/E",
    "W": "traffic/W"
}

light_status = {
    "N": "red",
    "S": "red",
    "E": "red",
    "W": "red"
}

root = tk.Tk()
root.title("Traffic Light Control via MQTT")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

circle_coords = {
    "N": canvas.create_oval(170, 50, 230, 110, fill="grey"),
    "S": canvas.create_oval(170, 290, 230, 350, fill="grey"),
    "E": canvas.create_oval(290, 170, 350, 230, fill="grey"),
    "W": canvas.create_oval(50, 170, 110, 230, fill="grey"),
}

def update_light_ui():
    color_map = {
        "red": "red",
        "yellow": "yellow",
        "green": "green"
    }
    for side, status in light_status.items():
        canvas.itemconfig(circle_coords[side], fill=color_map.get(status, "grey"))
    root.after(100, update_light_ui)

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    for side, topic in topics.items():
        client.subscribe(topic)

def on_message(client, userdata, msg):
    for side, topic in topics.items():
        if msg.topic == topic:
            payload = msg.payload.decode().lower()
            if payload in ["red", "yellow", "green"]:
                light_status[side] = payload

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
broker = "broker"
client.connect(broker, 1883, 60)

client.loop_start()
update_light_ui()
root.mainloop()



