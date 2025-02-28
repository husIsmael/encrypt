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
