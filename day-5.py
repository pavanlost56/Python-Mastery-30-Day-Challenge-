def reverse_string(s):
    """
    Reverses a given string.

    :param s: The string to be reversed.
    :return: The reversed string.
    """
    reversed_s=""
    for char in s:
        reversed_s = char + reversed_s
    return  reversed_s

# Sample Tests
print("hello =>", reverse_string("hello"))  # Expected Output: olleh
print("codedamn =>", reverse_string("codedamn"))  # Expected Output: nmadedoc
print("racecar =>", reverse_string("racecar"))  # Expected Output: racecar
print("12345 =>", reverse_string("12345"))  # Expected Output: 54321
