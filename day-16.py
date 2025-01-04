import re

def is_anagram(str1, str2):
    """
    Determine if the two strings are anagrams, considering case insensitivity and ignoring non-letter characters.
    """
    # Normalize strings: remove non-letter characters, convert to lowercase, and sort
    normalized_str1 = ''.join(sorted(re.sub(r'[^a-zA-Z]', '', str1).lower()))
    normalized_str2 = ''.join(sorted(re.sub(r'[^a-zA-Z]', '', str2).lower()))

    # Compare the normalized strings
    return normalized_str1 == normalized_str2

# Example function calls
print(is_anagram("Listen", "Silent"))  # Expected output: True
print(is_anagram("Hello", "World"))    # Expected output: False
print(is_anagram("Dormitory", "Dirty room"))  # Expected output: True
