import config
from wifi import do_connect
import machine
import dht
import json
import ntptime
import urequests
import time

def print_date(t):
    """Returns a isoformatted datetime string instead of a tuple"""
    ts = f"{t[0]}-{t[1]:0>2}-{t[2]:0>2}T{t[4]:0>2}:{t[5]:0>2}:{t[6]:0>2}"
    return ts

# Connect to the network
do_connect(config.WIFI_SSID, config.WIFI_PASSWORD)

# Set clock
rtc = machine.RTC()
ntptime.settime()

# Configure the sensors
d1 = dht.DHT11(machine.Pin(4))
d2 = dht.DHT11(machine.Pin(5))

# Turn on the LED
led = machine.Pin(2, machine.Pin.OUT)
led.on()

# Loop for hourly readings
while True:

    # Log measurements 
    d1.measure()
    d2.measure()
    t = rtc.datetime()
    response = json.dumps({
        "timestamp": print_date(t), 
        "temperature_sensor1": d1.temperature(), 
        "temperature_sensor2": d2.temperature()
    })

    # Post logged measurements to firebase
    urequests.post(config.FIREBASE_URL, data=response.encode())
    
    # Sleep for an hour
    time.sleep(60*60)