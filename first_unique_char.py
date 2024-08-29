"""
Write a function `first_unique_char(s)` that takes a string `s` and returns the index of the first non-repeating 
character. If there is no such character, return -1.
"""

def first_unique_char(s):
    # initializes a dictionary called char_count
    char_count = {}
    # initalizes the value of each char key, to be 0 and add 1 each time it is read in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Turn the s string into an iterable then loop through the characters to see if any of the characters
    # have a value of 1 in the dictionary, indicating it is unique, and returns the index value of the first unique
    # character
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    # If no unique character is found, returns -1
    return -1

print(first_unique_char("leetcode"))  # Should return 0
print(first_unique_char("loveleetcode"))  # Should return 2
print(first_unique_char("aabb"))  # Should return -1