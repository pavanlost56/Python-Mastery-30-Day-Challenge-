def is_prime_number(n):
    """
    Check if the provided number n is a prime number.
    Returns True if n is prime, and False otherwise.
    """
    if not isinstance(n, int) or n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            return False
    return True 

# Sample Function Calls for testing - Hit the run button to see the output
print(f"is_prime_number(3): {is_prime_number(3)}")  # Expected: True
print(f"is_prime_number(41): {is_prime_number(41)}")  # Expected: True
print(f"is_prime_number(6): {is_prime_number(6)}")  # Expected: False
print(f"is_prime_number(1): {is_prime_number(1)}")  # Expected: False
print(f"is_prime_number(-3): {is_prime_number(-3)}")  # Expected: False
print(f"is_prime_number(1.1): {is_prime_number(1.1)}")  # Expected: False

