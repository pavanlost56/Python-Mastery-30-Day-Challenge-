def get_hexcode(red, green, blue):
    """
    Converts RGB values to a hexadecimal color code.

    Parameters:
    red (int): Red component (0-255)
    green (int): Green component (0-255)
    blue (int): Blue component (0-255)

    Returns:
    str: Hexadecimal color code
    """
    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        raise ValueError("RGB values must be in the range 0-255.")

    return f"#{red:02X}{green:02X}{blue:02X}"

# Example function calls
print(get_hexcode(255, 0, 0))   # Output: #FF0000
print(get_hexcode(0, 255, 255)) # Output: #00FFFF
print(get_hexcode(0, 0, 0))     # Output: #000000
print(get_hexcode(201, 0, 210)) # Output: #C900D2
print(get_hexcode(255, 255, 255)) # Output: #FFFFFF
