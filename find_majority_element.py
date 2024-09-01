"""
Write a function `majority_element(nums)` that takes a list of integers `nums` and returns the majority element (the element 
that appears more than half the time). Assume that the array is non-empty and the majority element always exists.
"""

def majority_element(nums):
    majority_elem = {}

    for num in nums:
        # increment value of each unique number key
        majority_elem[num] = majority_elem.get(num, 0) + 1
    # majority will be the majority number
    majority = max(majority_elem.values())

    for num in majority_elem:
        # checks if the number key's value is the majority number
        if majority_elem[num] == majority:
            return num

print(majority_element([3, 2, 3]))  # Should return 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Should return 2