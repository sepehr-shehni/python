import os
import zipfile

def create_folder(folder_name):
    """
    Creates a folder with the given name in the current directory.
    
    Args:
    - folder_name (str): The name of the folder to create.
    """
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def zip_folder(folder_name, zip_name):
    """
    Zips the specified folder into a zip file.
    
    Args:
    - folder_name (str): The name of the folder to zip.
    - zip_name (str): The name of the zip file to create.
    """
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_name))

# Name of the folder to create
folder_name = "my_folder"
zip_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), "my_folder.zip")

# Create the folder
create_folder(folder_name)

# Zip the folder
zip_folder(folder_name, zip_name)

print(f"Folder '{folder_name}' has been zipped to '{zip_name}'.")
