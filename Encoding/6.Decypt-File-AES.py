from cryptography.fernet import Fernet
import os

def decrypt_file(encrypted_file_path, key):
    """Decrypt the specified file using the provided encryption key."""
    try:
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)

        decrypted_file_path = encrypted_file_path[:-10]  # Remove the ".encrypted" extension
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        return decrypted_file_path
    except Exception as e:
        # Handle decryption errors
        print("Error decrypting file:", e)
        return None

def main():
    """Main function to decrypt a file."""
    try:
        # Get input file path and encryption key from the user
        encrypted_file_path = input("Enter the path of the encrypted file: ").strip()  # Remove leading/trailing whitespace
        if not os.path.isfile(encrypted_file_path):
            print("Invalid file path or file does not exist.")
            return
        key = input("Enter the encryption key: ").strip()  # Remove leading/trailing whitespace

        # Decrypt the input file
        decrypted_file_path = decrypt_file(encrypted_file_path, key.encode())
        if decrypted_file_path:
            # Print the success message along with the decrypted file path
            print("File decrypted successfully.")
            print("Decrypted file saved at:", decrypted_file_path)
    except Exception as e:
        # Handle unexpected errors
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
