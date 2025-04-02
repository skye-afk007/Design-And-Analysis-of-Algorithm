#leetcode 2206
def canFormPairs(nums):
    # Create a dictionary to store the frequency of each number
    freq = {}
    
    # Count occurrences of each number
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Check if all counts are even
    for count in freq.values():
        if count % 2 != 0:
            return False
    return True

# Example usage
nums1 = [0, 0, 0, 0, 0]
print(canFormPairs(nums1)) 

nums2 = [1, 0, 1, 0, 2]
print(canFormPairs(nums2))  