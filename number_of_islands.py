"""
Task: Write a function `num_islands(grid)` that takes a 2D grid of `1`s (land) and `0`s (water), and returns the number of 
islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
"""

def num_islands(grid):
    if not grid:
        return 0
    
    def dfs(grid, i, j):
        # Check if the current position is out of bounds or is water ('0')
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        # Mark the current land as visited by setting it to '0'
        grid[i][j] = "0"
        # Visit all adjacent cells (up, down, left, right)
        dfs(grid, i - 1, j)  # up
        dfs(grid, i + 1, j)  # down
        dfs(grid, i, j - 1)  # left
        dfs(grid, i, j + 1)  # right

    island_count = 0
    # Traverse each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":  # If we find land, perform DFS
                island_count += 1
                dfs(grid, i, j)  # Mark all connected land as visited
    
    return island_count

print(num_islands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))  # Should return 3
