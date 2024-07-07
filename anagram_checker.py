"""
Write a function are_anagrams(s1, s2) that takes two strings s1 and s2 and returns True if they are anagrams of each other (they 
contain the same characters in any order) and False otherwise. The function should ignore case and non-alphanumeric characters.
"""

def are_anagrams(s1, s2):
    # Handles case sensitive issues, and remove any non-alphanumeric characters
    def clean_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    s1 = clean_string(s1)
    s2 = clean_string(s2)

    # if the strings are not same length then early calls False
    if len(s1) != len(s2):
        return False

    # Count characters
    count1 = {}
    count2 = {}

    # Tracks how many of a character occurs in the string
    for char in s1:
        count1[char] = count1.get(char, 0) + 1

    for char in s2:
        count2[char] = count2.get(char, 0) + 1

    # Compare counts
    return count1 == count2
    
are_anagrams("anagram", "nagaram")  # Should return True
are_anagrams("rat", "car")  # Should return False
are_anagrams("rat", "tar")  # Should return True
are_anagrams("race", "reca") # Should return True
are_anagrams("tatter", "totter") # Should return False