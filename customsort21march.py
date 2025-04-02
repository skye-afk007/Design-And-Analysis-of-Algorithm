def custom_sort(arr):
    arr1= []
    for i in range(len(arr)):
        if arr[i]!=0:
            arr1.append(arr[i])
    num=0
    for a in arr:
        if num==a:
            arr1.append(num)
    print(arr1)

arr=[0,1,0,2,3,5]
custom_sort(arr)     
        