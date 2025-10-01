import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

while True:
    user_input = input("Enter password length (or 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        break
    
    if user_input.isdigit():
        length = int(user_input)
        print("Generated Your VX Vault Key:", generate_password(length))
    else:
        print("Please type a number or 'exit'")
