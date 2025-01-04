def calculate_bmi(height, weight):
    """
    Calculate the Body Mass Index (BMI) and determine the BMI category.

    :param height: Height in centimeters.
    :param weight: Weight in kilograms.
    :return: A tuple containing the BMI value (rounded to two decimal places) and the BMI category.
    """
    # Convert height from centimeters to meters
    height_in_meters = height / 100

    # Calculate BMI
    bmi_value = weight / (height_in_meters ** 2)
    bmi_value = round(bmi_value, 2)

    # Determine the BMI category
    if bmi_value < 18.5:
        category = "underweight"
    elif 18.5 <= bmi_value <= 24.9:
        category = "healthy"
    elif 25 <= bmi_value <= 29.9:
        category = "overweight"
    else:
        category = "obese"

    return bmi_value, category

# Example function calls
print(calculate_bmi(155, 43.3))  # Expected: (18.02, "underweight")
print(calculate_bmi(170, 62.2))  # Expected: (21.52, "healthy")
print(calculate_bmi(150, 77.1))  # Expected: (34.27, "obese")
print(calculate_bmi(189, 101.2)) # Expected: (28.37, "overweight")
