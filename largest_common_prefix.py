"""
Write a function `longest_common_prefix(strs)` that takes a list of strings `strs` and returns the longest common prefix string amongst the strings. If there is no common prefix, return an empty string `""`.
"""

def longest_common_prefix(strs):
    if not strs:
        return ""  # Return an empty string if the input list is empty
    prefix = ""
    for char in strs[0]: # loops through all characters of first word in input list
        new_prefix = prefix + char # adds current char to the current prefix to check if new prefix
        # is shared among all words in the list
        shared = True  
        for word in strs:
            if word[0:len(new_prefix)] != new_prefix:
                # checks if the new prefix is the prefix of the word
                shared = False
                break
        if shared:
            # if the prefix is shared across all words then the character would
            # be added to the prefix variable
            prefix += char
        else:
            break
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))  # Should return "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))  # Should return ""