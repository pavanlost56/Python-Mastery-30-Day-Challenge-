def list_even_numbers(n):
    """
    Generate a list of even numbers from 1 to n (inclusive) using list comprehension.

    Parameters:
    n (int): The upper limit of the range

    Returns:
    list: A list of even numbers within the specified range
    """
    return [x for x in range(1, n + 1) if x % 2 == 0]

# Example function calls
print("Output for n=5:", list_even_numbers(5))
print("Output for n=30:", list_even_numbers(30))
print("Output for n=14:", list_even_numbers(14))
