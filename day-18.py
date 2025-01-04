def convert_distance(distance, unit):
    """
    Converts a distance between kilometers and meters.

    Parameters:
    - distance (float): The distance to be converted.
    - unit (str): The unit of the distance ('km' or 'mtr').

    Returns:
    - tuple: A tuple containing the converted distance and its unit.

    Raises:
    - ValueError: If the distance is negative or if the unit is invalid.
    """
    if distance < 0:
        raise ValueError("Distance cannot be negative.")

    if unit == "km":
        return distance * 1000, "mtr"
    elif unit == "mtr":
        return distance / 1000, "km"
    else:
        raise ValueError("Invalid unit. Use 'km' for kilometers or 'mtr' for meters.")

# Example function calls
print(convert_distance(1.5, "km"))  # Expected output: (1500.0, "mtr")
print(convert_distance(3000, "mtr"))  # Expected output: (3.0, "km")
print(convert_distance(0, "mtr"))  # Expected output: (0.0, "km")

# Uncomment the line below to test an error case
# print(convert_distance(-2, "mtr"))  # Expected output: ValueError
# print(convert_distance(5, "mile"))  # Expected output: ValueError
