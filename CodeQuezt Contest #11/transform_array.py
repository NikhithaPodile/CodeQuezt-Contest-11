def transform_array(arr):
    n = len(arr)
    if n == 0:
        return []

    # Sort the unique elements of the array
    sorted_unique_elements = sorted(set(arr))
    
    # Helper function to perform binary search
    def find_max_less_than(x):
        low, high = 0, len(sorted_unique_elements) - 1
        result = None
        while low <= high:
            mid = (low + high) // 2
            if sorted_unique_elements[mid] < x:
                result = sorted_unique_elements[mid]
                low = mid + 1
            else:
                high = mid - 1
        return result

    # Transform the array
    transformed_arr = []
    for num in arr:
        max_less_than = find_max_less_than(num)
        if max_less_than is None:
            transformed_arr.append(num)
        else:
            transformed_arr.append(max_less_than)
    
    return transformed_arr

# Sample Input
arr = [3, 5, 2, 8, 6]
transformed_arr = transform_array(arr)
print(transformed_arr)
