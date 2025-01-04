def square_numbers(numbers):
    """
    Squares each number in the given list.
    Integers are squared normally.
    Floating point numbers are squared and rounded to two decimal places.
    An empty list returns an empty list.
    """
    # Return a list comprehension with squared and rounded values
    return [round(num ** 2, 2) if isinstance(num, float) else num ** 2 for num in numbers]

# Example function calls and printing the output
print(square_numbers([2, 3]))          # Should return [4, 9]
print(square_numbers([-2, 2.3]))      # Should return [4, 5.29]
print(square_numbers([]))             # Should return []
