def largest_no(arr):
    
    temp = arr[0]
    for i in range(len(arr)):
        
        if arr[i] > temp:
            temp = arr[i]
    print(temp)  
    return temp  

arr = [1, 2, 5, 3]
largest_no(arr)

#primenumber

