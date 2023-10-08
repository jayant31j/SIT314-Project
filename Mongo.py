import serial
import requests
import threading
from pymongo import MongoClient
import certifi
import ssl


api_key = "PBHQ7J7LL22Y6WWE"
channel_url = "https://api.thingspeak.com/update"


mongo_uri = "mongodb+srv://user:hello@sit314.rih5xkn.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri, ssl=True)



db = client["test"]
collection = db["project"]


ser = serial.Serial('/dev/tty.usbmodem142201', 9600)  

def read_data():
    while True:
        try:
            data = ser.readline().decode().strip()
           
            print("Received data:", data)
           
            collection.insert_one({"data": data})

        except Exception as e:
            print("Error:", e)

def send_to_thingspeak():
    while True:
        try:
            distance = 0  
            status = ""   

       
            response = requests.post(channel_url, params={"api_key": api_key, "field1": distance, "field2": status})
            print("Data sent to ThingSpeak:", response.status_code)

        except Exception as e:
            print("Error:", e)

read_thread = threading.Thread(target=read_data)
send_thread = threading.Thread(target=send_to_thingspeak)

# Start the threads
read_thread.start()
send_thread.start()
