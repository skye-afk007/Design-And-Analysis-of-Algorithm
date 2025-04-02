
def remove_duplicates(input_array):
    unique_array = []
    for i in range(len(input_array)):
        is_duplicate = False
        for j in range(len(unique_array)):
            if input_array[i] == unique_array[j]:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_array.append(input_array[i])
    return unique_array

array = [1, 2, 3, 4, 1, 2, 3, 5]
unique_array = remove_duplicates(array)
print(unique_array)
