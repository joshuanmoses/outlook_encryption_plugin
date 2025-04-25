from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import base64
import os

def load_key(path):
    with open(path, 'rb') as f:
        return RSA.import_key(f.read())

def encrypt_message(message, public_key_path):
    # Generate a random AES-256 key
    aes_key = get_random_bytes(32)  # 32 bytes = 256 bits
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())

    # Encrypt AES key with RSA
    public_key = load_key(public_key_path)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    return {
        'encrypted_aes_key': base64.b64encode(encrypted_aes_key).decode(),
        'nonce': base64.b64encode(cipher_aes.nonce).decode(),
        'tag': base64.b64encode(tag).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode()
    }

def decrypt_message(data, private_key_path):
    private_key = load_key(private_key_path)
    cipher_rsa = PKCS1_OAEP.new(private_key)

    encrypted_aes_key = base64.b64decode(data['encrypted_aes_key'])
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    nonce = base64.b64decode(data['nonce'])
    tag = base64.b64decode(data['tag'])
    ciphertext = base64.b64decode(data['ciphertext'])

    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce)
    decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    return decrypted_message.decode()
