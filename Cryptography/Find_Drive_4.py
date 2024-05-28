import subprocess

def find_drive():
    drives = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "Z:", "N:", "K:", "L:", "X:", "P:", "U:", "J:", "S:", "R:", "W:", "Q:", "T:", "Y:", "I:", "O:", "V:", "M:"]
    system_drives = []

    try:
        cmd_output = subprocess.check_output("net share", shell=True)
        # Decode the output to string for both Python 2 and 3 compatibility
        cmd_output = cmd_output.decode()
        
        for drive in drives:
            if drive in cmd_output:
                system_drives.append(drive)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    return system_drives

drives = find_drive()

print(drives)

