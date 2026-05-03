import random
import string
def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be a positive number.")
            return
        print("\nInclude character types:")
        use_letters = input("Letters (y/n): ").lower() == 'y'
        use_digits = input("Numbers (y/n): ").lower() == 'y'
        use_symbols = input("Symbols (y/n): ").lower() == 'y'
        password = generate_password(length, use_letters, use_digits, use_symbols)
        if password is None:
            print("You must select at least one character type!")
        else:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter numeric values for length.")
if __name__ == "__main__":
    main()
