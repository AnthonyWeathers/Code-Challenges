"""
Write a function `find_missing_number(arr)` that takes a list of integers `arr` containing `n` distinct numbers taken from `0, 1, 2, ..., n` and returns the one number that is missing from the list.
"""

def find_missing_number(nums):
    # in order to make this work, the input list must have a number missing that would be inbetween the smallest number, usually 0
    # and the biggest number, in the case of a list having numbers from 0 - 9, then only a number from 1 - 8 can be missing for the 
    # result to be correct

    n = len(nums)
    
    # expected sum would be the sum of all numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    # returned result will be the missing number from the nums list
    return expected_sum - actual_sum

# Testing the function
print(find_missing_number([3, 0, 1]))  # Should return 2
print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Should return 8
print(find_missing_number([0]))  # Should return 1 (if the missing number is 1 in [0, 1])
print(find_missing_number([1]))  # Should return 0 (if the missing number is 0 in [0, 1])
print(find_missing_number([]))  # Should return 0 (if the list is empty, 0 is missing)
print(find_missing_number([9, 6, 4, 2, 3, 5, 10, 8, 13, 12, 7, 0, 1]))  # Should return 11