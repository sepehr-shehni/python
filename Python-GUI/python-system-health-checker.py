import psutil
import tkinter as tk

class SystemHealthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("System Health Checker")  # Set the title of the window

        # Create labels for displaying system health metrics
        self.cpu_label = tk.Label(root, text="CPU Usage:")
        self.cpu_label.pack()

        self.memory_label = tk.Label(root, text="Memory Usage:")
        self.memory_label.pack()

        self.ram_label = tk.Label(root, text="RAM Configuration:")
        self.ram_label.pack()

        self.network_label = tk.Label(root, text="Network Usage:")
        self.network_label.pack()

        self.disk_label = tk.Label(root, text="Disk Usage:")
        self.disk_label.pack()

        # Call the update_labels method to start displaying system metrics
        self.update_labels()

    def update_labels(self):
        # Retrieve system metrics using psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        ram_info = psutil.virtual_memory()
        network_info = psutil.net_io_counters()
        disk_info = psutil.disk_usage('/')

        # Update the labels with the latest system metrics
        self.cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        self.memory_label.config(text=f"Memory Usage: {memory_percent}%")
        self.ram_label.config(text=f"RAM Configuration: Total={ram_info.total} bytes, Available={ram_info.available} bytes")
        self.network_label.config(text=f"Network Usage: Sent={network_info.bytes_sent} bytes, Received={network_info.bytes_recv} bytes")
        self.disk_label.config(text=f"Disk Usage: Total={disk_info.total} bytes, Used={disk_info.used} bytes, Free={disk_info.free} bytes")

        # Schedule the update_labels method to run again after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_labels)

if __name__ == "__main__":
    # Create the Tkinter window
    root = tk.Tk()
    # Create an instance of the SystemHealthChecker class
    app = SystemHealthChecker(root)
    # Start the Tkinter event loop
    root.mainloop()


        