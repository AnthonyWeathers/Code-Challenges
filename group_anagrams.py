"""
Write a function `group_anagrams(strs)` that takes a list of strings `strs` and groups the anagrams together. Return the list of groups.
"""

def group_anagrams(strs):
    anagrams = {}

    # loops through list of words
    for s in strs:
        # Sort the string to use as a key
        sorted_str = ''.join(sorted(s))
        # Add the original string to the corresponding list in the dictionary
        if sorted_str not in anagrams: # if the sorted string is not in anagrams then an empty list will be created
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)

    # Return the list of groups of anagrams
    return list(anagrams.values())

# Testing the function
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Should return [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]