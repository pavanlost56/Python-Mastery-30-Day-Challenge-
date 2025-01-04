def unique_elements(lst):
    """
    Returns a new list containing unique elements from the input list, 
    preserving their original order. If the input is not a list or is empty, 
    handles accordingly.
    
    Parameters:
        lst (list): A list of elements (can be of any type).
    
    Returns:
        list: A new list with unique elements, maintaining the original order.
        None: If the input list is empty.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not lst:  # Check if the list is empty
        return None
    
    unique_set = set()
    unique_list = []
    
    for item in lst:
        if item not in unique_set:
            unique_set.add(item)
            unique_list.append(item)
    
    return unique_list

# Example function calls
if __name__ == "__main__":
    print(unique_elements([1, 2, 2, 3, 3, 3, 4]))  # Output: [1, 2, 3, 4]
    print(unique_elements(["apple", "banana", "apple", "orange", "banana"]))  # Output: ["apple", "banana", "orange"]
    print(unique_elements([]))  # Output: None
    try:
        print(unique_elements("not a list"))  # Should raise a TypeError
    except TypeError as e:
        print(e)
