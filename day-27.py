def fibonacci_numbers(N):
    """
    Return a tuple containing the (N-1)th, Nth, and (N+1)th Fibonacci numbers.
    For N <= 0, it handles edge cases as specified.
    """
    if N <= 0:
        if N == 0:
            return (-1, -1, 0)
        return (-1, -1, -1)

    # Function to calculate the Fibonacci sequence iteratively
    def calculate_fibonacci(num):
        a, b = 0, 1
        for _ in range(num):
            a, b = b, a + b
        return a

    if N == 1:
        return (-1, 0, 1)

    fib_n_minus_1 = calculate_fibonacci(N - 1)
    fib_n = calculate_fibonacci(N)
    fib_n_plus_1 = calculate_fibonacci(N + 1)

    return (fib_n_minus_1, fib_n, fib_n_plus_1)

# Example function calls
print(fibonacci_numbers(5))  # Expected: (3, 5, 8)
print(fibonacci_numbers(0))  # Expected: (-1, -1, 0)
print(fibonacci_numbers(-1)) # Expected: (-1, -1, -1)
print(fibonacci_numbers(4))  # Expected: (1, 3, 5)
print(fibonacci_numbers(1))  # Expected: (-1, 0, 1)
