def find_minimum(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
             
            right = mid       

    
    return nums[left]

rotated_sorted_array = [3,4,5,1,2]
print("The minimum number is:", find_minimum(rotated_sorted_array))


