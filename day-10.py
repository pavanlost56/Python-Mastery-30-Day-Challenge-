def is_leap_year(year):
    """
    Determines whether the specified year is a leap year.
    
    Args:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    # A year is a leap year if it is divisible by 4.
    # However, if the year is also divisible by 100, it is not a leap year unless it is divisible by 400.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example function calls
print("2000 is a leap year:", is_leap_year(2000))  # Expected output: True
print("1997 is a leap year:", is_leap_year(1997))  # Expected output: False
print("2024 is a leap year:", is_leap_year(2024))  # Expected output: True
