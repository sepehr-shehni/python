from cryptography.fernet import Fernet

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def encrypt_text(text, key):
    """Encrypt the input text using the provided encryption key."""
    try:
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt(text.encode())
        return encrypted_text
    except Exception as e:
        # Handle encryption errors
        print("Error encrypting text:", e)
        return None

def main():
    """Main function to encrypt user input."""
    try:
        # Get input text from the user
        text = input("Enter the text to encrypt: ").strip()  # Remove leading/trailing whitespace
        if not text:
            print("Input text cannot be empty.")
            return

        # Generate a new encryption key
        key = generate_key()

        # Encrypt the input text
        encrypted_text = encrypt_text(text, key)
        if encrypted_text:
            # Print the encrypted text and encryption key
            print("Encrypted text:", encrypted_text)
            print("Encryption key:", key)
    except Exception as e:
        # Handle unexpected errors
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
