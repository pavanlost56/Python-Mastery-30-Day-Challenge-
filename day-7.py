def factorial(n):
    """
    Calculate the factorial of a given positive integer n using recursion.
    """
    # Base case: if n is 1, return 1 (since 1! = 1)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Sample Tests
print("Factorial of 5:", factorial(5))   # Expected: 120
print("Factorial of 10:", factorial(10))  # Expected: 3628800
print("Factorial of 8:", factorial(8))   # Expected: 40320
print("Factorial of 18:", factorial(18))  # Expected: 6402373705728000
