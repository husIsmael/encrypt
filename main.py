from Crypto.Cipher import AES
import base64
import os

def pad(s):
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encrypt(raw, key):
    try:
        raw = pad(raw)
        iv = os.urandom(AES.block_size)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode('utf-8'))).decode('utf-8')
    except Exception as e:
        print(f"Encryption error: {e}")
        raise

def decrypt(enc, key):
    try:
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
    except Exception as e:
        print(f"Decryption error: {e}")
        raise

def main():
    while True:
        key = input("Enter encryption key (16/24/32 characters): ").strip()
        print(f"Captured key: '{key}'")  # Debug print to show the exact input
        print(f"Key length: {len(key)}")  # Debug print
        if len(key) not in [16, 24, 32]:
            print("Invalid key length. Please enter a key of length 16, 24, or 32 characters.")
            continue
        break

    while True:
        print("Select operation:")
        print("1. Encrypt")
        print("2. Decrypt")

        choice = input("Enter choice(1/2): ")

        if choice == '1':
            plaintext = input("Enter text to encrypt: ")
            encrypted = encrypt(plaintext, key)
            print(f"Encrypted text: {encrypted}")
        elif choice == '2':
            encrypted = input("Enter text to decrypt: ")
            try:
                decrypted = decrypt(encrypted, key)
                print(f"Decrypted text: {decrypted}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid input")
            continue

if __name__ == "__main__":
    main()