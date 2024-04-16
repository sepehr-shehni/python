import base64

def encode_text(text):
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded_text

def main():
    text = input("Enter the text to encode: ")
    encoded_text = encode_text(text)
    print("Encoded text:", encoded_text)

if __name__ == "__main__":
    main()
