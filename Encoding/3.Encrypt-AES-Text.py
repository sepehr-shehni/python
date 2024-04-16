from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_text(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode())
    return encrypted_text

def main():
    text = input("Enter the text to encrypt: ")
    key = generate_key()
    encrypted_text = encrypt_text(text, key)
    print("Encrypted text:", encrypted_text)
    print("Encryption key:", key)

if __name__ == "__main__":
    main()
