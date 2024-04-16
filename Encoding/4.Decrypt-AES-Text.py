from cryptography.fernet import Fernet

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text.decode()

def main():
    encrypted_text = input("Enter the encrypted text: ")
    key = input("Enter the encryption key: ")
    decrypted_text = decrypt_text(encrypted_text.encode(), key.encode())
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
