from cryptography.fernet import Fernet

def write_key():
    """Generates a key and saves it into a file"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the current directory named `key.key`"""
    return open("key.key", "rb").read()

# Generate and write a new key
write_key()
def encrypt_file(filename, key):
    """Given a filename (str) and key (bytes), it encrypts the file and writes it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Load the key
key = load_key()
# Encrypt the file
encrypt_file("example.txt", key)


def decrypt_file(filename, key):
    """Given a filename (str) and key (bytes), it decrypts the file and writes it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Load the key
key = load_key()
# Decrypt the file
decrypt_file("example.txt", key)
