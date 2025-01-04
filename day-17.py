def simple_interest(principal, rate, time):
    """
    Calculate the simple interest for given principal, rate, and time.
    
    Args:
    principal (float): The initial amount of money.
    rate (float): The interest rate in percentage.
    time (float): The time period in years.

    Returns:
    float: The simple interest calculated, rounded to two decimal places.
    """
    # Calculate the simple interest
    interest = (principal * rate * time) / 100
    # Round the result to two decimal places
    return round(interest, 2)

# Example function calls
print("Example 1:", simple_interest(23000, 4, 7))  # Expected output: 6440.0
print("Example 2:", simple_interest(10000, 1, 10)) # Expected output: 1000.0
print("Example 3:", simple_interest(100000, 5, 4)) # Expected output: 20000.0
