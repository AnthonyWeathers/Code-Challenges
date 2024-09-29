"""
Write a function `rotate_image(matrix)` that takes a 2D matrix and rotates it 90 degrees (clockwise).
"""

def rotate_image(matrix):
    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix

print(rotate_image([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))
# Should modify matrix to:
# [
#  [7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]
# ]
