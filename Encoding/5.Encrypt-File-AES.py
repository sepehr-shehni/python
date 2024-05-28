from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt the specified file using the provided encryption key."""
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(data)

        encrypted_file_path = file_path + '.encrypted'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        return encrypted_file_path
    except Exception as e:
        # Handle encryption errors
        print("Error encrypting file:", e)
        return None

def main():
    """Main function to encrypt a file."""
    try:
        # Get input file path from the user
        file_path = input("Enter the path of the file to encrypt: ").strip()  # Remove leading/trailing whitespace
        if not os.path.isfile(file_path):
            print("Invalid file path or file does not exist.")
            return

        # Generate a new encryption key
        key = generate_key()

        # Encrypt the input file
        encrypted_file_path = encrypt_file(file_path, key)
        if encrypted_file_path:
            # Print the success message along with the encrypted file path and encryption key
            print("File encrypted successfully.")
            print("Encrypted file saved at:", encrypted_file_path)
            print("Encryption key:", key)
    except Exception as e:
        # Handle unexpected errors
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
