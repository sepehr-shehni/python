from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()
print(f"Generated Key: {key.decode()}")  # Print the key for later decryption

# Initialize the Fernet object with the generated key
f = Fernet(key)

# The text to be encrypted
text = "Hello World"

# Encrypt the text (ensure it is in bytes)
encrypted_text = f.encrypt(text.encode())

print(f"Encrypted Text: {encrypted_text.decode()}")

# Uncomment and use the below lines to use a predefined key and encrypted text
# key = b"m8WrcrKNKa81MAz0XpPukZzK4Aawm18QTPT6XLYGlMs="
# encrypted_text = b"gAAAAABfxmSz0bC7OG6jP3zBCzgnP6ypK_z1VbUj3hs9dQBvLHrkI3Lh_iLfUINli8evK8cJOXJf5MeX8R_AXdohY5ht_gNWZQ=="
