import random
import string

def generate_password():

    password_length = int(input("Enter the required length of password: "))

    all_chars = string.ascii_letters + string.digits + string.punctuation
    

    password = ''.join(random.choice(all_chars) for c in range(password_length))
    
    return password


password = generate_password()

print(f"Generated password: {password}")
