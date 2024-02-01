import gc
import board
import microcontroller
import time
import ssl
import socketpool
import wifi
import adafruit_ntp
import rtc
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import json
import keypad
from ideaboard import IdeaBoard

ib = IdeaBoard()

key_pins = (board.IO27,)
pot = ib.AnalogIn(board.IO33)

keys = keypad.Keys(key_pins, value_when_pressed=False)

try:
    from secrets2 import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

#broker_username = secrets["broker_username"]
#broker_key = secrets["broker_key"]
deviceid = secrets["deviceid"]
topic = secrets["topic"]

print("Connecting to %s" % secrets["ssid"])
try:
    wifi.radio.connect(secrets["ssid"], secrets["password"])
except:
    time.sleep(10)
    microcontroller.reset()
print("Connected to %s!" % secrets["ssid"])

def hard_reset():
    print("Resetting...")
    time.sleep(10)
    microcontroller.reset()

# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connect(mqtt_client, userdata, flags, rc):
    # This function will be called when the mqtt_client is connected
    # successfully to the broker.
    print("Connected to MQTT Broker!")
    print("Flags: {0}\n RC: {1}".format(flags, rc))
    mqtt_client.subscribe(topic + "/CMD/" + deviceid)
    payload = {"status": "online"}
    payload = json.dumps(payload)
    mqtt_client.publish(topic + "/BIRTH/" + deviceid, payload)


def disconnect(mqtt_client, userdata, rc):
    # This method is called when the mqtt_client disconnects
    # from the broker.
    print("Disconnected from MQTT Broker!")


def subscribe(mqtt_client, userdata, topic, granted_qos):
    # This method is called when the mqtt_client subscribes to a new feed.
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))


def unsubscribe(mqtt_client, userdata, topic, pid):
    # This method is called when the mqtt_client unsubscribes from a feed.
    print("Unsubscribed from {0} with PID {1}".format(topic, pid))


def publish(mqtt_client, userdata, topic, pid):
    # This method is called when the mqtt_client publishes data to a feed.
    print(f"Published to {topic}")


def message(client, topic, message):
    # Method called when a client's subscribed feed has a new value.
    print("New message on topic {0}: {1}".format(topic, message))
    if message:
        if message == "ON":
            ib.pixel = (0,0,255)
        if message == "OFF":
            ib.pixel = (0,0,0)
            

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Create Network Time Protocol connection
ntp = adafruit_ntp.NTP(pool, tz_offset=0)

# Set the internal time
rtc.RTC().datetime = ntp.datetime

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=secrets["broker"],
    port=secrets["port"],
    #username=secrets["broker_username"],
    #password=secrets["broker_key"],
    socket_pool = pool,
    ssl_context=ssl.create_default_context()
)

payload = {"status": "offline"}
payload = json.dumps(payload)
mqtt_client.will_set(topic + "/DEATH/" + deviceid, payload)

# Setup the callback methods above
mqtt_client.on_connect = connect
mqtt_client.on_disconnect = disconnect
mqtt_client.on_message = message
mqtt_client.on_subscribe = subscribe
mqtt_client.on_unsubscribe = unsubscribe
mqtt_client.on_publish = publish

# Connect the client to the MQTT broker.
print("Connecting to broker...")
mqtt_client.connect()

last = time.monotonic()
while True:
    mqtt_client.loop(timeout=0)
    event = keys.events.get()
    if event:
        if event.pressed:
            payload = {"switch": "ON"}
            payload = json.dumps(payload)
            mqtt_client.publish(topic + "/switch/" + deviceid, payload, retain=True)
        if event.released:
            payload = {"switch": "OFF"}
            payload = json.dumps(payload)
            mqtt_client.publish(topic + "/switch/" + deviceid, payload, retain=True)
    if time.monotonic() - last > 10:
        valor = pot.value
        timestamp = time.time()
        payload = {"pot": valor, "timestamp": timestamp}
        payload = json.dumps(payload)
        mqtt_client.publish(topic + "/DATA/" + deviceid, payload)
        last = time.monotonic()