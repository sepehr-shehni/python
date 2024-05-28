import base64

def decode_text(encoded_text):
    """Decode the input text using base64 decoding."""
    try:
        # Decode the base64-encoded text using UTF-8 encoding
        decoded_text = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
        return decoded_text
    except Exception as e:
        # Handle decoding errors
        print("Error decoding text:", e)
        return None

def main():
    """Main function to decode user input."""
    try:
        # Get input encoded text from the user
        encoded_text = input("Enter the encoded text: ").strip()  # Remove leading/trailing whitespace
        if not encoded_text:
            print("Input encoded text cannot be empty.")
            return

        # Decode the input encoded text
        decoded_text = decode_text(encoded_text)
        if decoded_text:
            # Print the decoded text
            print("Decoded text:", decoded_text)
    except Exception as e:
        # Handle unexpected errors
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
