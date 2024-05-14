import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine character sets
    all_chars = lowercase_letters + uppercase_letters + digits + symbols

    # Generate password
    password = ''.join(random.sample(all_chars, length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password you'd like to generate: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
