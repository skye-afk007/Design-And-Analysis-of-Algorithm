def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  
            right = mid - 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


array = [1, 2, 2, 2, 3, 4]
target = 2
print(find_first_occurrence(array, target))  