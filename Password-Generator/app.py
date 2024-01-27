import random
import string


def generate_password(
    length,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_special=True,
):
    # Define the character sets based on user preferences
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Check if at least one character set is selected
    if not characters:
        print(
            "Please include at least one character type (uppercase, lowercase, digits, or special characters)."
        )
        return None

    # Generate the password using random.choice
    password = "".join(random.choice(characters) for _ in range(length))

    return password


def check_strength(
    password, include_uppercase, include_lowercase, include_digits, include_special
):
    # Check the strength of the password based on included character types
    has_upper = any(char.isupper() for char in password) if include_uppercase else True
    has_lower = any(char.islower() for char in password) if include_lowercase else True
    has_digit = any(char.isdigit() for char in password) if include_digits else True
    has_special = (
        any(char in string.punctuation for char in password)
        if include_special
        else True
    )

    # Evaluate strength based on included character types
    strength = "Weak"
    if has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif has_upper and has_lower and has_digit:
        strength = "Moderate"

    return strength


def main():
    # Prompt the user to specify the desired length of the password
    password_length = int(input("Enter the desired length of the password: "))

    # Prompt the user to choose which character types to include
    include_uppercase = input("Include Uppercase Letters? (y/n): ").lower() == "y"
    include_lowercase = input("Include Lowercase Letters? (y/n): ").lower() == "y"
    include_digits = input("Include Digits? (y/n): ").lower() == "y"
    include_special = input("Include Special Characters? (y/n): ").lower() == "y"

    # Generate the password
    password = generate_password(
        password_length,
        include_uppercase,
        include_lowercase,
        include_digits,
        include_special,
    )

    if password:
        # Display the generated password
        print("Generated Password:", password)

        # Check and display the strength of the password
        strength = check_strength(
            password,
            include_uppercase,
            include_lowercase,
            include_digits,
            include_special,
        )
        print("Password Strength:", strength)


if __name__ == "__main__":
    main()
