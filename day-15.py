def common_elements(list1, list2):
    """
    This function takes two lists as input and returns a list of elements that are common to both lists.
    If there are no common elements, it returns an empty list.
    """
    return list(set(list1) & set(list2))

# Example function calls and printing their outputs
# Test Case 1: Two Common Elements
print("Test Case 1:", common_elements([1, 2, 3, 4], [2, 5, 6, 1]))

# Test Case 2: No Common Elements
print("Test Case 2:", common_elements([1, 2, 3], [4, 5, 6]))

# Test Case 3: Both Lists are Identical
print("Test Case 3:", common_elements([1, 2, 3], [1, 2, 3]))

# Test Case 4: Four Common Elements
print("Test Case 4:", common_elements([1, 2, 3, 4, 7, 8], [2, 4, 6, 1, 3, 9]))
