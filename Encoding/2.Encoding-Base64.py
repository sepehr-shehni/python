import base64

def decode_text(encoded_text):
    decoded_text = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
    return decoded_text

def main():
    encoded_text = input("Enter the encoded text: ")
    decoded_text = decode_text(encoded_text)
    print("Decoded text:", decoded_text)

if __name__ == "__main__":
    main()
