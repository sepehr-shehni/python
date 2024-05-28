import base64

def encode_text(text):
    """Encode the input text using base64 encoding."""
    try:
        # Encode the text using UTF-8 encoding and base64 encoding
        encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        return encoded_text
    except Exception as e:
        # Handle encoding errors
        print("Error encoding text:", e)
        return None

def main():
    """Main function to encode user input."""
    try:
        # Get input text from the user
        text = input("Enter the text to encode: ").strip()  # Remove leading/trailing whitespace
        if not text:
            print("Input text cannot be empty.")
            return

        # Encode the input text
        encoded_text = encode_text(text)
        if encoded_text:
            # Print the encoded text
            print("Encoded text:", encoded_text)
    except Exception as e:
        # Handle unexpected errors
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

