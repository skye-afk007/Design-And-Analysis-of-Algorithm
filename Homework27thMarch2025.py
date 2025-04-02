#rotate an array 3 times
#[1,2,3,4,5,6]og
#[2,3,4,5,6,1]
#[3,4,5,6,1,2]
#[4,5,6,1,2,3]
def rotate_array(arr, rotations):
    n = len(arr)
    if rotations>n:
        rotations=rotations%n
    for i in range(rotations):
        arr.append(arr.pop(0))
        print(arr)


array = [1, 2, 3, 4, 5, 6]
rotate_array(array, 10) 