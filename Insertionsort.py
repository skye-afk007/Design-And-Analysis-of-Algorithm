def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1

        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  


numbers = [17, 65, 51, 23, 21,20] 
print("Original array:", numbers)

insertion_sort(numbers)
print("Sorted array:", numbers)



