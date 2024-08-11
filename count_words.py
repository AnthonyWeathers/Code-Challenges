"""
Write a function `count_words(s)` that takes a string `s` and returns the number of words in the string. 
Words are separated by spaces.
"""

def count_words(str):
    # use split to separate the string into a list of words 
    words = str.split()
    # return the length of the list, matching the number of words
    return len(words)

print(count_words("Hello world"))  # Should return 2
print(count_words("Count the number of words in this sentence"))  # Should return 8