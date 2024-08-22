"""
Write a function `rotate_array(nums, k)` that takes a list of integers `nums` and an integer `k`, and rotates the list to the right 
by `k` steps.
"""

def rotate_array(nums, k):
    # initialized a new list with same number of indexes as input list nums
    new_nums = [0] * len(nums)

    for i in range(len(nums)):
        # if the current index plus the k shift value would go outside the list's range
        # then would subtract the length of the nums list to get the index if it wrapped around
        if i + k >= len(nums):
            new_nums[(i + k) - len(nums)] = nums[i]
        else:
            new_nums[i + k] = nums[i]
    return new_nums

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # Should return [5, 6, 7, 1, 2, 3, 4]
print(rotate_array([-1, -100, 3, 99], 2))  # Should return [3, 99, -1, -100]
