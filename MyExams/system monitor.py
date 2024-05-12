import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_graph(frame):
    # Get CPU, memory, disk, and network usage percentages
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_usage = (psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv) / 1024  # Convert to KB

    # Append new data to lists for each usage
    cpu_usage.append(cpu_percent)
    memory_usage.append(memory_percent)
    disk_usage.append(disk_percent)
    network_usage_list.append(network_usage)

    # Clear the plots and plot the new data
    axs[0].clear()
    axs[0].plot(cpu_usage, 'r')
    axs[0].set_title('CPU Usage (%)')
    axs[0].text(len(cpu_usage)-1, cpu_percent, f'{cpu_percent}%', verticalalignment='bottom', horizontalalignment='right')

    axs[1].clear()
    axs[1].plot(memory_usage, 'g')
    axs[1].set_title('Memory Usage (%)')
    axs[1].text(len(memory_usage)-1, memory_percent, f'{memory_percent}%', verticalalignment='bottom', horizontalalignment='right')

    axs[2].clear()
    axs[2].plot(disk_usage, 'b')
    axs[2].set_title('Disk Usage (%)')
    axs[2].text(len(disk_usage)-1, disk_percent, f'{disk_percent}%', verticalalignment='bottom', horizontalalignment='right')

    axs[3].clear()
    axs[3].plot(network_usage_list, 'y')
    axs[3].set_title('Network Usage (KB)')
    axs[3].text(len(network_usage_list)-1, network_usage, f'{network_usage:.2f} KB', verticalalignment='bottom', horizontalalignment='right')

    plt.subplots_adjust(hspace=0.5)

    # Reset the scales of the plots
    for ax in axs:
        ax.relim()
        ax.autoscale_view()

# Create a Tkinter window
root = tk.Tk()
root.title('System Monitor')

# Create plots using Matplotlib
fig, axs = plt.subplots(4, 1, figsize=(8, 6))

# Lists to store system resource usage data
cpu_usage = []
memory_usage = []
disk_usage = []
network_usage_list = []

# Create an animation to update the data
ani = animation.FuncAnimation(fig, update_graph, interval=1000, blit=False)

# Create a Matplotlib canvas and display it in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the main Tkinter event loop
root.mainloop()
