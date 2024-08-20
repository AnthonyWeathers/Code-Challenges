"""
Write a function `find_intersection(nums1, nums2)` that takes two lists of integers `nums1` and `nums2` and returns a list of their 
intersection. Each element in the result must be unique.
"""

def find_intersection(nums1, nums2):
    # convert the arrays into sets, removing any repeated numbers in them
    set1 = set(nums1)
    set2 = set(nums2)
    # use the intersection method of set to find the shared values between set1 and set2
    intersection = list(set1.intersection(set2))

    return intersection

print(find_intersection([1, 2, 2, 1], [2, 2]))  # Should return [2]
print(find_intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Should return [4, 9]