def time_difference(start, end):
    start_hours,start_minutes=map(int,start.split(":"))
    end_hours,end_minutes=map(int,end.split(":"))
    start_total_minutes=start_hours*60+start_minutes
    end_total_minutes=end_hours*60+end_minutes
    if end_total_minutes<start_total_minutes:
        end_total_minutes +=24*60
    total_difference_minutes=end_total_minutes -start_total_minutes
    hours=total_difference_minutes // 60
    minutes=total_difference_minutes % 60
    return {"hours":hours,"minutes":minutes}

# Example function calls and print statements
print(time_difference('2:25', '3:00'))  # Expected Output: {'hours': 0, 'minutes': 35}
print(time_difference('23:15', '00:30')) # Expected Output: {'hours': 1, 'minutes': 15}
print(time_difference('5:30', '5:30')) # Expected Output: {'hours': 0, 'minutes': 0}