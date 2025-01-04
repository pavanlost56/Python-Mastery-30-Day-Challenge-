def is_power_of_two(number):
    if number <= 0:
        return False
    # Check if only one bit is set in the binary representation
    return (number & (number - 1)) == 0

# Test cases as examples
print("is_power_of_two(4):", is_power_of_two(4))  # Should return True
print("is_power_of_two(6):", is_power_of_two(6))  # Should return False
print("is_power_of_two(8):", is_power_of_two(8))  # Should return True
print("is_power_of_two(7):", is_power_of_two(7))  # Should return False
print("is_power_of_two(1):", is_power_of_two(1))  # Should return True (2^0)
print("is_power_of_two(0):", is_power_of_two(0))  # Should return False (Edge case)
