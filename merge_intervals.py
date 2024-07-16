"""
Write a function merge_intervals(intervals) that takes a list of intervals represented as pairs of integers and merges all overlapping intervals.
"""

def merge_intervals(intervals):
    # if intervals is empty
    if not intervals:
        return []

    # Sort intervals based on the first number of each interval in case
    # intervals is out of order, example: [[2, 5], [1, 3]]
    intervals.sort(key=lambda x: x[0])
    # merged is initalized to first interval of sorted intervals
    merged = [intervals[0]]
    # loops with current set to 2nd interval onward till the last interval of intervals
    for current in intervals[1:]:
        # sets last_merged to the last interval of the merged list
        last_merged = merged[-1]
        # Check if there is an overlap between the current interval's starting value and the end value of the last interval 
        # in merged
        if current[0] <= last_merged[1]: 
            # sets end value of last_merged to the higher end value between last_merged and current
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # appends the current interval to the merged list
            merged.append(current)

    return merged

# Testing the function
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Should return [[1, 6], [8, 10], [15, 18]]

print(merge_intervals([[1, 4], [4, 5]]))
# Should return [[1, 5]]

print(merge_intervals([[1, 2], [4, 8], [5, 13], [9, 16], [17, 21], [20, 22]]))
# Should return [[1, 2], [4, 16], [17, 22]]