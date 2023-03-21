import string
import random

def generate_key():
    # generate a random key
    chars = list(string.ascii_uppercase)
    random.shuffle(chars)
    return dict(zip(string.ascii_uppercase, chars))

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char in key:
            # substitute character using the key
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext.upper():
        if char in key:
            # substitute character using the key
            plaintext += key[char]
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = "Gusti Alantyastito Ahnaf"
key = generate_key()
ciphertext = encrypt(plaintext, key)

print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
