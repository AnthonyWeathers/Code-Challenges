"""
Write a function `top_k_frequent(nums, k)` that takes a list of integers `nums` and an integer `k`, and returns the `k` most frequent elements.
"""

def top_k_frequent(nums, k):
    # Step 1: Build the frequency dictionary
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Step 2: Sort the dictionary by frequency and get the top k elements
    sorted_freq = sorted(frequency, key=frequency.get, reverse=True)

    # Step 3: Return the top k most frequent elements (with there being multiple sharing
    # the least frequency but still apart of the top numbers, it would take the first ones
    # it gets)
    return sorted_freq[:k]

print(top_k_frequent([2, 5, 0, 7, 4, 3, 2, 6, 4, 2], 3))
print(top_k_frequent([1, 4, 1, 1, 2, 2, 3], 2))  # Should return [1, 2]
print(top_k_frequent([1], 1))  # Should return [1]