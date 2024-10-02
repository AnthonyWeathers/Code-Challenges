"""
Write a function `subarray_sum(nums, k)` that takes a list of integers `nums` and an integer `k`, and returns the total 
number of continuous subarrays whose sum equals to `k`.
"""

def subarray_sum(nums, k):
    subarrays_sum = 0

    # Iterate over all starting points of potential subarrays
    for i in range(len(nums)):
        current_sum = 0  # Reset current sum for each new subarray start
        # loop from start of new subarray to end of remaining array
        for j in range(i, len(nums)):
            current_sum += nums[j]
            print(f'Subarray from index {i} to {j}: sum = {current_sum}')
            if current_sum == k:
                subarrays_sum += 1
    
    return subarrays_sum

print(subarray_sum([1, 1, 1], 2))  # Should return 2