from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    return encrypted_file_path

def main():
    file_path = input("Enter the path of the file to encrypt: ")
    key = generate_key()
    encrypted_file_path = encrypt_file(file_path, key)
    print("File encrypted successfully.")
    print("Encrypted file saved at:", encrypted_file_path)
    print("Encryption key:", key)

if __name__ == "__main__":
    main()
