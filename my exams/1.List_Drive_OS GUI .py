import tkinter as tk
from tkinter import scrolledtext
import os

def get_drives():
    drives = []
    if os.name == "nt":
        drives = [chr(i) + ":" for i in range(65, 91) if os.path.exists(chr(i) + ":")]
    elif os.name == "posix":
        with open("/proc/mounts", "r") as f:
            drives = [line.split()[1] for line in f if line.startswith("/dev/")]
    return drives

def display_drives():
    drive_list.delete(1.0, tk.END)
    drives = get_drives()
    for drive in drives:
        drive_list.insert(tk.END, drive + '\n')

# Create the main window
root = tk.Tk()
root.title("List of Drives")

# Create a scrolled text widget to display the list of drives
drive_list = scrolledtext.ScrolledText(root, width=30, height=10, wrap=tk.WORD)
drive_list.pack(padx=10, pady=10)

# Button to refresh the list of drives
refresh_button = tk.Button(root, text="Refresh", command=display_drives)
refresh_button.pack(pady=5)

# Display the initial list of drives
display_drives()

# Run the application
root.mainloop()
