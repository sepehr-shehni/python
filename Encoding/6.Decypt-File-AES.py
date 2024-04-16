from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    
    decrypted_file_path = encrypted_file_path[:-10]  # Remove the ".encrypted" extension
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    return decrypted_file_path

def main():
    encrypted_file_path = input("Enter the path of the encrypted file: ")
    key = input("Enter the encryption key: ")
    decrypted_file_path = decrypt_file(encrypted_file_path, key.encode())
    print("File decrypted successfully.")
    print("Decrypted file saved at:", decrypted_file_path)

if __name__ == "__main__":
    main()
