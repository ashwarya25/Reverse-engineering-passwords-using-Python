target_hash = '5e884898da28047151d0e56f8dc6292773603d0d4e1c9b9b7164b4c7c5d908dd'  # Example hash

with open('hashed_passwords.txt', 'r') as file:
    for line in file:
        password, hashed = line.strip().split(': ')
        if hashed == target_hash:
            print(f'The password is: {password}')
            break
