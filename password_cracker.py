import hashlib

def load_passwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        passwords = file.read().splitlines()
    return passwords

def load_salts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        salts = file.read().splitlines()
    return salts

def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

def crack_sha1_hash(sha1_hash_to_crack, use_salts=False):
    passwords = load_passwords('top-10000-passwords.txt')
    salts = load_salts('known-salts.txt') if use_salts else []

    # Check passwords without salts
    for password in passwords:
        if sha1_hash(password) == sha1_hash_to_crack:
            return password

    # Check passwords with salts if use_salts is True
    if use_salts:
        for password in passwords:
            for salt in salts:
                # Salt before the password
                if sha1_hash(salt + password) == sha1_hash_to_crack:
                    return password
                # Salt after the password
                if sha1_hash(password + salt) == sha1_hash_to_crack:
                    return password

    return "PASSWORD NOT IN DATABASE"