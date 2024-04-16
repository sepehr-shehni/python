import psutil

def list_drives():
    """
    Lists all drives available on the system.
    
    Returns:
    - list: A list of drive names.
    """
    drives = psutil.disk_partitions(all=True)
    drive_names = [drive.device for drive in drives if drive.device]
    return drive_names

# List all drives
drives = list_drives()
print("Drives on the system:")
for drive in drives:
    print(drive)
