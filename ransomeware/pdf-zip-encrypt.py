import os
import subprocess
from cryptography.fernet import Fernet
import shutil
import zipfile

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        original_data = file.read()
    encrypted_data = cipher_suite.encrypt(original_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Function to recursively search for PDF files in all drives
def find_pdf_files():
    pdf_files = []
    for root, dirs, files in os.walk('/', topdown=True):
        for name in files:
            if name.endswith('.pdf'):
                pdf_files.append(os.path.join(root, name))
    return pdf_files

# Function to copy PDF files to a folder
def copy_files_to_folder(files, folder):
    for file in files:
        shutil.copy(file, folder)

# Function to zip a folder
def zip_folder(folder, zip_filename):
    shutil.make_archive(zip_filename, 'zip', folder)

# Find all PDF files in all drives
pdf_files = find_pdf_files()

# Create a directory to store copied files
copy_folder = 'copied_pdfs'
os.makedirs(copy_folder, exist_ok=True)

# Copy PDF files to the directory
copy_files_to_folder(pdf_files, copy_folder)

# Zip the copied folder
zip_filename = 'pdf_files.zip'
zip_folder(copy_folder, zip_filename)

# Encrypt the zip file
encrypt_file(zip_filename, key)

print("Process completed successfully!")
