from cryptography.fernet import Fernet
# Generating a key
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    
    with open('key.key', "wb") as key_file:
        key_file.write(key)
    print('Key Generated!!!')
# loading our key
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open('key.key', "rb").read()
# function for encrypting our file
def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def encrypt_file():
    file = input('File name: ')
    key = load_key()
    encrypt(file,key)
    print('File Encrypted!!!')
# function for decrypting our file
def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def decrypt_file():
    file = input('File name: ')
    key = load_key()
    decrypt(file,key)
    print('File Decrypted!!!')


