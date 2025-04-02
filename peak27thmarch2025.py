#peak element is bigger than its left and right neighbors
def find_peak_linear(arr):
    n=len(arr)

    if n==1:
        return arr[0]
    if arr[0]>=arr[1]:
        return arr[0]
    if arr[n-1]>=arr[n-2]:
        return arr[n-1]
    for i in range(1,n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i
    return -1

array=[1,2,5,3,4]
peak_index = find_peak_linear(array)
print(f"The peak element is {array[peak_index]} at index {peak_index}.")