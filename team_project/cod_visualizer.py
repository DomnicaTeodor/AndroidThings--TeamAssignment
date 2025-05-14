import socket
import threading
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time

SERVER_IP = '192.168.1.134'
SERVER_PORT = 1234

MAX_POINTS = 100 

class DistanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Distance Monitor")

        self.data = []
        self.timestamps = []

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Distance Over Time")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Distance (cm)")
        self.line, = self.ax.plot([], [], 'b-')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.socket_thread = threading.Thread(target=self.socket_client, daemon=True)
        self.socket_thread.start()

        self.update_plot()

    def socket_client(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print(f"Connecting to {SERVER_IP}:{SERVER_PORT}...")
                s.connect((SERVER_IP, SERVER_PORT))
                print("Connected.")

                while True:
                    data = s.recv(8)
                    if not data:
                        break
                    try:
                        value = str(data.decode('utf-8'))
                        value = float(value) 
                        timestamp = time.strftime('%H:%M:%S')

                        self.data.append(value)
                        self.timestamps.append(timestamp)
                        
                        if value < 40:
                            print("INTRUDER DETECTED")

                        # Limit data size
                        if len(self.data) > MAX_POINTS:
                            self.data.pop(0)
                            self.timestamps.pop(0)

                    except ValueError:
                        continue  # Ignore bad data

        except Exception as e:
            print("Socket error:", e)

    def update_plot(self):
        if self.data:
            self.line.set_data(range(len(self.data)), self.data)
            self.ax.set_xlim(0, len(self.data) if len(self.data) > 10 else 10)
            self.ax.set_ylim(0, 100)
            self.canvas.draw()

        self.root.after(100, self.update_plot) 


if __name__ == "__main__":
    root = tk.Tk()
    app = DistanceApp(root)
    root.mainloop()