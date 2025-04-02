def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        greater_than_pivot = [x for x in array[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5, 4, 5]
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)

