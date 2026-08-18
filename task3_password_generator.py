import random
import string


def generate_password(length):
    """Generate a random password of the requested length."""

    if length < 4:
        return "Password length must be at least 4."

    # Characters that can be used in the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Make sure the password contains at least
    # one uppercase letter, one lowercase letter,
    # one number, and one special character.
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Add remaining random characters
    all_characters = uppercase + lowercase + digits + special_characters

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password so the first four characters
    # are not always in the same order.
    random.shuffle(password)

    return "".join(password)


def main():
    print("=" * 50)
    print("           PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))

            if length < 4:
                print("Please enter a length of at least 4.")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

            again = input("\nGenerate another password? (y/n): ").strip().lower()

            if again != "y":
                print("\nThank you for using the Password Generator!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
