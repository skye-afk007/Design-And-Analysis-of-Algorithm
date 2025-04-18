def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    else:
        pivot = arr[len(arr) // 2]  
        left = [x for x in arr if x < pivot]  
        middle = [x for x in arr if x == pivot]  
        right = [x for x in arr if x > pivot]  

        
        return quick_sort(left) + middle + quick_sort(right)


numbers = [10, 7, 8, 9, 1, 5]
print("Original array:", numbers)

sorted_numbers = quick_sort(numbers)
print("Sorted array:", sorted_numbers)
