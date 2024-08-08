"""
Write a function `two_sum(nums, target)` that takes a list of integers `nums` and an integer `target`, and returns the indices of the 
two numbers that add up to `target`.
"""

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None # Occurs if no two indexes sum up to the target

print(two_sum([2, 7, 11, 15], 9))  # Should return [0, 1]
print(two_sum([3, 2, 4], 6))  # Should return [1, 2]
print(two_sum([2, 7, 9, 11, 3, 5, 17, 4], 26)) # Should return [2, 6]