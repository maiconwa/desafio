from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    try:
        open("secret.key", "rb").read()
    except IOError:
        generate_key()
    return open("secret.key", "rb").read()


def encrypt_message(message, key):
    encoded_message = message.encode()
    f = Fernet(key)
    encrypt_message = f.encrypt(encoded_message)
    return encrypt_message


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypt_message_message = f.decrypt(encrypted_message)
    return decrypt_message_message
