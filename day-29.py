def count_vowels(input_string):
    """
    Counts the occurrences of each vowel in the given string.

    Args:
    input_string (str): The string in which vowels are to be counted.

    Returns:
    dict: A dictionary with vowels as keys and their counts as values.
    """
    # Initialize a dictionary with vowels as keys and 0 as their initial counts
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the input string to lowercase to make the function case-insensitive
    input_string = input_string.lower()

    # Iterate over each character in the string
    for char in input_string:
        if char in vowels:
            vowels[char] += 1

    return vowels

# Example function calls and printing their outputs
if __name__ == "__main__":
    example1 = count_vowels("Hello World")
    print("Hello World =>", example1)

    example2 = count_vowels("Python Programming is Awesome")
    print("Python Programming is Awesome =>", example2)

    example3 = count_vowels("Myths")  # String with no vowels
    print("Myths =>", example3)
