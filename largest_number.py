"""
Write a function `find_largest(numbers)` that takes a list of integers `numbers` and returns the largest number in the list.
"""

def find_largest(num_list):
    if not num_list:  # Check if the list is empty
        return None  # Return None for an empty list

    largest = num_list[0]  # Initialize largest variable to the first element of the list

    # loops through the entire list
    for num in num_list:
        # uses max to check the higher number between num and largest and assigns it to largest
        largest = max(largest, num)

    return largest

print(find_largest([1, 2, 3, 4, 5])) # Should return 5
print(find_largest([10, 9, 8, 7, 6]))  # Should return 10
print(find_largest([-1, -2, -3, -4, -5]))  # Should return -1
print(find_largest([5]))  # Should return 5
print(find_largest([]))  # Should return None