import random
import string

def generate_password(length=6, letters_count=2, numbers_count=2, symbols_count=2):
    # Validate the input to ensure the length is sufficient
    if length < letters_count + numbers_count + symbols_count:
        raise ValueError("Length must be greater than or equal to the sum of letters, numbers, and symbols count.")

    # Generate random characters for each category
    letters = random.choices(string.ascii_letters, k=letters_count)
    numbers = random.choices(string.digits, k=numbers_count)
    symbols = random.choices(string.punctuation, k=symbols_count)

    # Combine all characters
    password_characters = letters + numbers + symbols

    # Fill the remaining length with random choices from all character types if needed
    remaining_length = length - len(password_characters)
    if remaining_length > 0:
        password_characters += random.choices(
            string.ascii_letters + string.digits + string.punctuation, k=remaining_length
        )

    # Shuffle the characters to make the password random
    random.shuffle(password_characters)

    # Return the final password as a string
    return ''.join(password_characters)

# Test cases
print(generate_password(length=8, letters_count=3, numbers_count=3, symbols_count=2))  # Example output: a2#b4c5?
print(generate_password())  # Example output: 1d$2e#
try:
    print(generate_password(length=6, letters_count=3, numbers_count=3, symbols_count=2))  # Should raise ValueError
except ValueError as e:
    print(e)
print(generate_password(length=10, letters_count=4, numbers_count=3, symbols_count=3))  # Example output: A1b2C#D$3
