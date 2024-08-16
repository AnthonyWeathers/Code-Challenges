"""
Write a `function merge_sorted_lists(l1, l2)` that takes two sorted lists `l1` and `l2` and returns a single sorted list by merging them.
"""

def merge_sorted_lists(l1, l2):
    merged = []
    i, j = 0, 0

    # loops until one of the lists are completely read through
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            # appends the value at index i of l1 if the value is smaller than or equal to j of l2
            merged.append(l1[i])
            i += 1
        else:
            # occurs if j of l2 is smaller than i of l1
            merged.append(l2[j])
            j += 1

    # Append remaining elements, this is to grab the remaining values from the list with values that haven't been added yet
    merged.extend(l1[i:])
    merged.extend(l2[j:])

    return merged

print(merge_sorted_lists([1, 2, 4], [1, 3, 4]))  # Should return [1, 1, 2, 3, 4, 4]
print(merge_sorted_lists([5, 6, 7], [1, 2, 3]))  # Should return [1, 2, 3, 5, 6, 7]
print(merge_sorted_lists([], [1, 2, 3]))  # Should return [1, 2, 3]
print(merge_sorted_lists([5, 6, 7], []))  # Should return [5, 6, 7]