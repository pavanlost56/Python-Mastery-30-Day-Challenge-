def convert_temperature(value, input_unit, output_unit):
    """
    Convert a temperature value from one unit to another.

    Parameters:
    value (float): The temperature value to convert.
    input_unit (str): The unit of the input value ('c', 'f', 'k').
    output_unit (str): The unit to convert to ('c', 'f', 'k').

    Returns:
    float: The converted temperature, rounded to two decimal places.
    """
    # If input and output units are the same, return the value
    if input_unit == output_unit:
        return round(value, 2)

    # Celsius conversions
    if input_unit == 'c':
        if output_unit == 'f':  # Celsius to Fahrenheit
            return round((value * 9/5) + 32, 2)
        elif output_unit == 'k':  # Celsius to Kelvin
            return round(value + 273.15, 2)

    # Fahrenheit conversions
    if input_unit == 'f':
        if output_unit == 'c':  # Fahrenheit to Celsius
            return round((value - 32) * 5/9, 2)
        elif output_unit == 'k':  # Fahrenheit to Kelvin
            return round((value + 459.67) * 5/9, 2)

    # Kelvin conversions
    if input_unit == 'k':
        if output_unit == 'c':  # Kelvin to Celsius
            return round(value - 273.15, 2)
        elif output_unit == 'f':  # Kelvin to Fahrenheit
            return round((value * 9/5) - 459.67, 2)

    # If input_unit or output_unit is invalid, behavior is undefined
    raise ValueError("Invalid input or output unit. Use 'c', 'f', or 'k'.")

# Example function calls
print(convert_temperature(25, 'c', 'f'))  # Celsius to Fahrenheit
print(convert_temperature(10, 'c', 'k'))  # Celsius to Kelvin
print(convert_temperature(300, 'k', 'c'))  # Kelvin to Celsius
print(convert_temperature(273, 'k', 'f'))  # Kelvin to Fahrenheit
print(convert_temperature(68, 'f', 'k'))  # Fahrenheit to Kelvin
print(convert_temperature(32, 'f', 'c'))  # Fahrenheit to Celsius
