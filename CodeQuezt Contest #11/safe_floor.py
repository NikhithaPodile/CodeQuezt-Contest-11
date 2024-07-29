def safe_floor(n, test_rows, test_columns, tests):
    # Binary search to find the highest safe floor
    low, high = 0, test_rows - 1
    highest_safe_floor = -1
    
    while low <= high:
        mid = (low + high) // 2
        floor, result = tests[mid]
        
        if result == 0:
            highest_safe_floor = floor
            low = mid + 1
        else:
            high = mid - 1
    
    return highest_safe_floor

# Sample Input
n = 6
test_rows = 2
test_columns = 2
tests = [
    [3, 0],
    [6, 1]
]

# Calling the function with the sample input
print(safe_floor(n, test_rows, test_columns, tests))  # Output: 3
