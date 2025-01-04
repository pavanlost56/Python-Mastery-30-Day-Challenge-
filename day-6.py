from statistics import mean, mode , median ,multimode 
def central_tendency(data):
    """
    Calculate the mean, median, and mode of a list of numbers.
    
    Parameters:
    data (list): A list of numerical data.

    Returns:
    dict: A dictionary containing the mean, median, and mode.
    """
    # calculate mean 
    mean_value = round(mean(data),2)
    # calculate median 
    median_value = round(median(data),2)
    # calculate mode
    modes = multimode(data)
    mode_value = min(modes)

    results = {
        "mean": mean_value,
        "mode": mode_value,
        "median": median_value
    }

    print(results)
    
    return results

# Example function calls
print("Example 1:", central_tendency([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
print("Example 2:", central_tendency([5, 7, 12, 15, 21, 23, 23, 30, 34, 36, 40, 45, 50, 55]))
print("Example 3:", central_tendency([1, 1, 2, 3, 4, 5, 8, 13]))