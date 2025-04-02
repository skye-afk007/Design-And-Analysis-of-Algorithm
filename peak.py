def find_all_peaks(arr):
    n = len(arr)
    peaks = []

    
    if n == 1:
        return [0]
    if arr[0] >= arr[1]:
        peaks.append(0)
    if arr[n-1] >= arr[n-2]:
        peaks.append(n-1)
    
    
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            peaks.append(i)
    
    return peaks


array = [1, 3, 20, 4, 5, 1]
peak_indices = find_all_peaks(array)
print(f"The peaks are at indices {peak_indices}, with values {[array[i] for i in peak_indices]}.")