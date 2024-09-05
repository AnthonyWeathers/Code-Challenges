"""
Write a function `max_subarray_sum(nums)` that takes a list of integers `nums` and returns the sum of the largest contiguous subarray.
"""

def max_subarray_sum(nums):
    # Initialize current_sum and max_sum with the first element of the list
    current_sum = nums[0]
    max_sum = nums[0]

    # Iterate through the list starting from the second element
    for num in nums[1:]:
        # Update current_sum: either start a new subarray or continue the current one
        # Depends on if the current num is greater than the sum plus current num
        current_sum = max(num, current_sum + num)

        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Should return 6 (subarray is [4,-1,2,1])
print(max_subarray_sum([1]))  # Should return 1
print(max_subarray_sum([-1, -2, -3, -4]))  # Should return -1 (subarray is [-1])
