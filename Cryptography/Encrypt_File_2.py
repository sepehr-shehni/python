from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()
print(f"Generated Key: {key.decode()}")  # Print the key for later decryption

# Initialize the Fernet object with the generated key
f = Fernet(key)

# Read the contents of the file to be encrypted
try:
    with open("1.jpg", "rb") as file:
        data = file.read()
except FileNotFoundError:
    print("The file '1.jpg' was not found.")
    exit()

# Encrypt the data
encrypted_data = f.encrypt(data)

# Write the encrypted data to a new file
try:
    with open("1enc.jpg", "wb") as new_file:
        new_file.write(encrypted_data)
except Exception as e:
    print(f"An error occurred while writing the encrypted file: {e}")
    exit()

print("File encrypted successfully and saved as '1enc.jpg'.")
