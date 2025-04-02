def find_all_peaks_binary_search(arr, low, high):
    peaks = []
    n = len(arr)

    if low <= high:
        mid = (low + high) // 2

        
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            peaks.append(mid)

        
        peaks += find_all_peaks_binary_search(arr, low, mid - 1)
        peaks += find_all_peaks_binary_search(arr, mid + 1, high)

    return peaks


array = [1, 3, 20, 4, 7, 0]
peak_indices = find_all_peaks_binary_search(array, 0, len(array) - 1)
print(f"The peaks are at indices {peak_indices}, with values {[array[i] for i in peak_indices]}.")