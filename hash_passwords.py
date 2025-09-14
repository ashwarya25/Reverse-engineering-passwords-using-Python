import hashlib

# Read the password list
with open('passwords.txt', 'r') as file:
    passwords = file.readlines()

# Hash each password using SHA-256 and write to hashed_passwords.txt
with open('hashed_passwords.txt', 'w') as file:
    for password in passwords:
        password = password.strip()  # Remove any leading/trailing whitespace
        hash_object = hashlib.sha256(password.encode())
        hex_dig = hash_object.hexdigest()
        file.write(f'{password}: {hex_dig}\n')

print('Passwords have been hashed and saved to hashed_passwords.txt')
