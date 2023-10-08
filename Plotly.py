import serial
import plotly.graph_objs as go
import plotly.offline as pyo
import threading
import tkinter as tk
import re


data = [go.Scatter(x=[], y=[], mode='lines', name='Distance')]
layout = go.Layout(title='Arduino Data Visualization')
fig = go.Figure(data=data, layout=layout)


x_data = []
y_data = []


ser = serial.Serial('/dev/tty.usbmodem142201', 9600)  


stop_threads = False

def read_data():
    while not stop_threads:
        try:
            data = ser.readline().decode().strip()

            distance_match = re.search(r'\d+', data)

            if distance_match:
                distance = float(distance_match.group())

                x_data.append(len(x_data) + 1)
                y_data.append(distance)

                fig.data[0].x = x_data
                fig.data[0].y = y_data

                pyo.plot(fig, filename='arduino_data.html')

        except Exception as e:
            print("Error:", e)

def start_plotly_server():
    pyo.plot(fig, filename='arduino_data.html')

def stop_threads_func():
    global stop_threads
    stop_threads = True


root = tk.Tk()
root.title("Arduino Data Visualization")

stop_button = tk.Button(root, text="Stop", command=stop_threads_func)
stop_button.pack()


read_thread = threading.Thread(target=read_data)
plotly_thread = threading.Thread(target=start_plotly_server)


read_thread.start()
plotly_thread.start()


root.mainloop()
