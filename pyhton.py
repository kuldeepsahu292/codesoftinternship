import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Invalid input. Please enter a positive integer.")
            return

        generated_password = generate_password(password_length)
        print("Generated password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
