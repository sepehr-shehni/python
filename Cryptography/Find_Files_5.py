import subprocess

def find_drive():
    # List of possible drive letters
    drives = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "Z:", "N:", "K:", "L:", "X:", "P:", "U:", "J:", "S:", "R:", "W:", "Q:", "T:", "Y:", "I:", "O:", "V:", "M:"]
    system_drives = []

    try:
        # Execute the 'net share' command to list shared resources
        cmd_output = subprocess.check_output("net share", shell=True).decode()
        
        # Check each drive letter if it is present in the command output
        for drive in drives:
            if drive in cmd_output:
                system_drives.append(drive)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return system_drives

def find_files(drives, extensions):
    # Open the file to write the paths of found files
    with open("File_Path.txt", "w") as f:
        # Search for files in the root directory
        for ext in extensions:
            try:
                # Execute the command to find all files with the given extension in the root directory
                cmd_output = subprocess.check_output(f"cd / && dir /S /B *.{ext}", shell=True).decode()
                # Write the found file paths to the file
                f.write(cmd_output)
                print(ext)
            except subprocess.CalledProcessError:
                pass
            except Exception as e:
                print(f"An error occurred: {e}")

        # Search for files in each of the system drives
        for drive in drives:
            for ext in extensions:
                try:
                    # Execute the command to find all files with the given extension in the specific drive
                    cmd_output = subprocess.check_output(f"{drive} && dir /S /B *.{ext}", shell=True).decode()
                    # Write the found file paths to the file
                    f.write(cmd_output)
                    print(f"{ext} ------- {drive}")
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"An error occurred: {e}")

# Define the file extensions to search for
extensions = ["jpg", "txt", "pdf"]

# Find the system drives
drives = find_drive()

# Find the files with the specified extensions in the system drives and root directory
find_files(drives, extensions)

