def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_zero = set()  # Keep track of rows to set to 0
    col_zero = set()  # Keep track of columns to set to 0

    # Step 1: Identify rows and columns with zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)

    # Step 2: Set rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if i in row_zero or j in col_zero:
                matrix[i][j] = 0

# Example usage
matrix = [[1, 2, 3],
          [4, 0, 6],
          [7, 8, 9]]

setZeroes(matrix)
print(matrix) 