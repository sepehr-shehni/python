import tkinter as tk
from tkinter import scrolledtext
import psutil

def get_drives_info():
    drives_info = []
    for partition in psutil.disk_partitions():
        drive = partition.device
        fs_type = partition.fstype
        try:
            usage = psutil.disk_usage(drive)
            total_size = usage.total / (1024 * 1024 * 1024)  # Convert to GB
            free_size = usage.free / (1024 * 1024 * 1024)  # Convert to GB
            drives_info.append((drive, fs_type, total_size, free_size))
        except PermissionError:
            # Ignore permission errors
            pass
    return drives_info

def display_drives_info():
    drive_info_list.delete(1.0, tk.END)
    drives_info = get_drives_info()
    for drive_info in drives_info:
        drive, fs_type, total_size, free_size = drive_info
        drive_info_list.insert(tk.END, f"Drive: {drive}\n")
        drive_info_list.insert(tk.END, f"File System Type: {fs_type}\n")
        drive_info_list.insert(tk.END, f"Total Size: {total_size:.2f} GB\n")
        drive_info_list.insert(tk.END, f"Free Space: {free_size:.2f} GB\n\n")

# Create the main window
root = tk.Tk()
root.title("Drive Information")

# Create a scrolled text widget to display the drive information
drive_info_list = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
drive_info_list.pack(padx=10, pady=10)

# Button to refresh the drive information
refresh_button = tk.Button(root, text="Refresh", command=display_drives_info)
refresh_button.pack(pady=5)

# Display the initial drive information
display_drives_info()

# Run the application
root.mainloop()
