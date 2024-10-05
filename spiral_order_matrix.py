"""
Write a function `spiral_order(matrix)` that takes a 2D matrix and returns all the elements of the matrix in spiral order.
"""

def spiral_order(matrix):
    result = []
    
    if not matrix:
        return result
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result


print(spiral_order([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])) 
# Should return [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(spiral_order([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
])) 
# Should return [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
