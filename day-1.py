def convert_binary(binary_string):
    if not binary_string.startswith('0b'):
        raise ValueError("Input must be a binary string starting with '0b' ")
    binary_part=binary_string[2:]
    decimal_value=0
    for i, bit in enumerate(reversed(binary_part)):
        if bit not in {'0','1'}:
           raise ValueError("Input contains invalid characters for a binary string")
        decimal_value+= int(bit) * (2 ** i )
    return decimal_value

# Example function calls and output printing
print("Decimal of '0b101':", convert_binary('0b101'))        # Expected Output: 5
print("Decimal of '0b0':", convert_binary('0b0'))            # Expected Output: 0
print("Decimal of '0b11101010':", convert_binary('0b11101010'))  # Expected Output: 234

