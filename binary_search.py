"""
Write a function `binary_search(nums, target)` that takes a sorted list of integers `nums` and a target value `target`, and returns the index of `target` in the list. If `target` is not found, return `-1`.
"""

def binary_search(nums, target):
    # if target exists in nums, then gets index value
    # otherwise sets index to -1
    if target in nums:
        index = nums.index(target)
    else:
        index = -1
    return index

print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))  # Should return 3
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8))  # Should return -1
print(binary_search([1, 7, 3, 6, 16, 2, 13], 2))  # Should return -1
print(binary_search([8, 11, 5, 2, 12, 3, 6, 21], 11))  # Should return -1