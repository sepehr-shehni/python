import psutil
import ctypes
import os
import sys

def get_drive_info():
    """
    Gets information about all drives on the system.
    
    Returns:
    - list of dicts: A list of dictionaries containing drive information.
    """
    drive_info = []
    drives = psutil.disk_partitions(all=True)
    for drive in drives:
        try:
            usage = psutil.disk_usage(drive.mountpoint)
            info = {
                "drive": drive.device,
                "filesystem": drive.fstype,
                "total_size": convert_bytes(usage.total),
                "free_space": convert_bytes(usage.free)
            }
            drive_info.append(info)
        except PermissionError:
            print(f"PermissionError: Unable to access drive {drive.device}.")
    return drive_info

def convert_bytes(bytes, precision=2):
    """
    Converts bytes to a human-readable format.
    
    Args:
    - bytes (int): The number of bytes.
    - precision (int): The number of decimal places to include in the result.
    
    Returns:
    - str: The size in a human-readable format.
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    bytes = float(bytes)
    for unit in units:
        if bytes < 1024.0:
            return f"{bytes:.{precision}f} {unit}"
        bytes /= 1024.0

# Check if running with administrative privileges
def run_as_admin():
    if sys.platform.startswith('win'):
        try:
            if ctypes.windll.shell32.IsUserAnAdmin():
                return
            hinstance = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            if hinstance <= 32:
                raise ctypes.WinError(hinstance)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print("This function is only supported on Windows.")
        sys.exit(1)

# Get information about all drives
try:
    drive_info = get_drive_info()
except PermissionError:
    print("PermissionError: Unable to access drives. Running the program as admin...")
    run_as_admin()
    try:
        drive_info = get_drive_info()
    except PermissionError:
        print("PermissionError: Still unable to access drives even with admin privileges.")

# Print drive information
for drive in drive_info:
    print("Drive:", drive["drive"])
    print("Filesystem:", drive["filesystem"])
    print("Total Size:", drive["total_size"])
    print("Free Space:", drive["free_space"])
    print()
