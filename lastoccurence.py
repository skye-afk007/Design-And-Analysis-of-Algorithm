def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1  

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid  
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1  # Target must be in the right half
        else:
            high = mid - 1  # Target must be in the left half

    return result