import os
import hashlib
import shutil
import zipfile
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('encryption.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Load the encryption key
def load_key():
    return open('encryption.key', 'rb').read()

# Find duplicate files by comparing their hashes
def find_duplicates(directory):
    hash_dict = {}
    duplicates = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash in hash_dict:
                duplicates.append(file_path)
            else:
                hash_dict[file_hash] = file_path
    return duplicates

# Compute the hash of a file
def hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Move duplicate files to a specific folder
def move_duplicates(duplicates, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for file in duplicates:
        shutil.move(file, dest_folder)

# Compress the folder into a zip file
def compress_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

# Encrypt the zip file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Main function
def main():
    # Define the source directory and destination folder for duplicates
    source_directory = 'path/to/your/directory'
    duplicates_folder = 'duplicates'
    zip_filename = 'duplicates.zip'

    # Find duplicate files
    duplicates = find_duplicates(source_directory)
    print(f'Found {len(duplicates)} duplicate files.')

    # Move duplicates to the duplicates folder
    move_duplicates(duplicates, duplicates_folder)
    print(f'Moved duplicates to {duplicates_folder}.')

    # Compress the duplicates folder
    compress_folder(duplicates_folder, zip_filename)
    print(f'Compressed duplicates into {zip_filename}.')

    # Generate and load the encryption key
    key = generate_key()
    print(f'Encryption key generated and saved.')

    # Encrypt the zip file
    encrypt_file(zip_filename, key)
    print(f'Encrypted the zip file {zip_filename}.')

if __name__ == '__main__':
    main()