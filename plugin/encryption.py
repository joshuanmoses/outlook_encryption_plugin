from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def load_key(path):
    with open(path, 'rb') as f:
        return RSA.import_key(f.read())

def encrypt_message(message, public_key_path):
    key = load_key(public_key_path)
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(message.encode())

def decrypt_message(ciphertext, private_key_path):
    key = load_key(private_key_path)
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(ciphertext).decode()
