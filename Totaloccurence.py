def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def total_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)
    if first == -1 or last == -1:
        return 0  
    return last - first + 1


array = [1, 2, 2, 2, 3, 4, 5]
target = 2

count = total_occurrences(array, target)
print(f"The total occurrences of {target} is {count}.")

array = [1, 2, 2, 2, 3, 4]
target = 2
total_occurrences(array, 2)


