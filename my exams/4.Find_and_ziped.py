import os
import shutil
import zipfile
import psutil

def search_and_copy_txt_files(dest_dir):
    """
    Search for all .txt files in all drives of the system and copy them to the destination directory.
    Then, zip the destination directory.
    
    Args:
    - dest_dir (str): The destination directory to copy .txt files and zip.
    """
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Destination directory '{dest_dir}' created successfully.")

    # Search for .txt files in all drives
    for drive in get_system_drives():
        for root, dirs, files in os.walk(drive):
            for file in files:
                if file.endswith('.txt'):
                    source_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_dir, file)
                    shutil.copyfile(source_file, dest_file)
                    print(f"File '{file}' copied to '{dest_dir}'.")

    # Zip the destination directory
    zip_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), "txt_files.zip")
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(dest_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), dest_dir))
    print(f"Destination directory '{dest_dir}' has been zipped to '{zip_name}'.")

def get_system_drives():
    """
    Get a list of all drives in the system.
    
    Returns:
    - list: A list of drive letters (e.g., ['C:', 'D:', ...]).
    """
    return [drive.device for drive in psutil.disk_partitions()]

# Define destination directory
destination_directory = "txt_files"

# Search for .txt files in all drives, copy them to the destination directory, and zip the destination directory
search_and_copy_txt_files(destination_directory)
