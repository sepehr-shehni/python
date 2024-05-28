from cryptography.fernet import Fernet

# Define the decryption key
key = "vsgDfJ8ZDKP8vT2dMXnRNyzcKvBasBhgO9pF7HQvAiA="

# Initialize the Fernet object
f = Fernet(key)

# Open the encrypted file and read its data
try:
    with open("1enc.jpg", "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
except FileNotFoundError:
    print("The file '1enc.jpg' was not found.")
    exit()

# Decrypt the data
try:
    decrypted_data = f.decrypt(encrypted_data)
except Exception as e:
    print(f"An error occurred during decryption: {e}")
    exit()

# Write the decrypted data to a new file
try:
    with open("1.jpg", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
    exit()

print("File decrypted successfully and saved as '1.jpg'.")




