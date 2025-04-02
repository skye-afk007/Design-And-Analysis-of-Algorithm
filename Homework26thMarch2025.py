#find square root of a number using binary search


def square_root_binary_search(num, precision=0.00001):
    if num < 0:
        return None  
    
    
    low, high = 0, max(1, num)
    mid = 0
    
    
    while high - low > precision:
        mid = (low + high) / 2
        if mid * mid < num:
            low = mid
        else:
            high = mid
    
    return mid


number = 25
result = square_root_binary_search(number)
print(f"The square root of {number} is approximately {result:.5f}")