from cryptography.fernet import Fernet

def decrypt_text(encrypted_text, key):
    """Decrypt the input text using the provided encryption key."""
    try:
        cipher = Fernet(key)
        decrypted_text = cipher.decrypt(encrypted_text)
        return decrypted_text.decode()
    except Exception as e:
        # Handle decryption errors
        print("Error decrypting text:", e)
        return None

def main():
    """Main function to decrypt user input."""
    try:
        # Get input encrypted text and encryption key from the user
        encrypted_text = input("Enter the encrypted text: ").strip()  # Remove leading/trailing whitespace
        if not encrypted_text:
            print("Encrypted text cannot be empty.")
            return
        key = input("Enter the encryption key: ").strip()  # Remove leading/trailing whitespace
        if not key:
            print("Encryption key cannot be empty.")
            return

        # Decrypt the input encrypted text
        decrypted_text = decrypt_text(encrypted_text.encode(), key.encode())
        if decrypted_text:
            # Print the decrypted text
            print("Decrypted text:", decrypted_text)
    except Exception as e:
        # Handle unexpected errors
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
