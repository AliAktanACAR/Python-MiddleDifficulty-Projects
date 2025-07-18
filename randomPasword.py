import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "Please select at least one character type!"

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator")
    
    try:
        length = int(input("Enter password length (e.g., 20): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols (!@#...)? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    print(f"\n🔑 Generated Password: {password}")

if __name__ == "__main__":
    main()
