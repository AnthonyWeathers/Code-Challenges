"""
Write a function `move_zeroes(nums)` that takes a list of integers `nums` and moves all 0's to the end while maintaining the relative order of the non-zero elements.
"""

def move_zeroes(nums):
    # if input is an empty list
    if not nums:
        return []
    
    zeroes = []
    numbers = []
    for i in range(len(nums)):
        # when an index is 0
        if nums[i] == 0:
            zeroes.append(nums[i])
        else:
            numbers.append(nums[i])
    """ combines the list of numbers and zeroes into a newly ordered
    list where all zeroes are at the back while maintaining the 
    relative order of the other numbers """
    ordered = numbers + zeroes

    return ordered

print(move_zeroes([0, 1, 0, 3, 12])) # Should modify list to [1, 3, 12, 0, 0]
print(move_zeroes([8, 0, 4, 6, 0, 12, 0, 9])) # Should modify list to [8, 4, 6, 12, 9, 0, 0, 0]
print(move_zeroes([ 0, 9])) # Should modify list to [9, 0]