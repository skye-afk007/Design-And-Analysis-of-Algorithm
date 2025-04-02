def rotate_matrix_90(matrix):
    
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    
    rotated = [row[::-1] for row in transpose]
    
    
    print("Original Matrix:")
    for row in matrix:
        print(row)
    
    print("\nRotated Matrix (90 degrees clockwise):")
    for row in rotated:
        print(row)


matrix = [[1, 2, 3],
          [4, 5, 6],      
          [7, 8, 9]]
rotate_matrix_90(matrix) 

