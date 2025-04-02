#MATRIX

def matrix_transpose(matrix):
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("\nTranspose:")
    for row in transpose:
        print(row)

# Example Usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_transpose(matrix)                   