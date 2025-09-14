import hashlib

# Define the legitimate password
legitimate_password = 'JohnDoe!1990'  # You can change this to any password you want to test

# Generate its hash
hash_object = hashlib.sha256(legitimate_password.encode())
legitimate_hash = hash_object.hexdigest()

# Display the generated hash
print(f'Generated Hash for "{legitimate_password}": {legitimate_hash}')

# Open the hashed_passwords file and compare
found = False
with open('hashed_passwords.txt', 'r') as file:
    for line in file:
        password, hashed = line.strip().split(': ')
        if hashed == legitimate_hash:
            print(f'The password is: {password}')
            found = True
            break

if not found:
    print('Password not found in the list.')
