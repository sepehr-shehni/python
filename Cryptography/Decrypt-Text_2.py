from cryptography.fernet import Fernet

# Define the decryption key
key = "m8WrcrKNKa81MAz0XpPukZzK4Aawm18QTPT6XLYGlMs="

# The encrypted message
encrypted_message = "gAAAAABfxmSz0bC7OG6jP3zBCzgnP6ypK_z1VbUj3hs9dQBvLHrkI3Lh_iLfUINli8evK8cJOXJf5MeX8R_AXdohY5ht_gNWZQ=="

# Initialize the Fernet object
f = Fernet(key)

try:
    # Decrypt the message
    decrypted_message = f.decrypt(encrypted_message.encode())
    # Print the decrypted message
    print(decrypted_message.decode())  # Assuming the decrypted message is a string
except Exception as e:
    print(f"An error occurred during decryption: {e}")
