"""
Write a function 'length_of_longest_substring(s)' that takes a string 's' and returns the length of the longest substring without repeating 
characters.
"""

def length_of_longest_substring(str):
    substr = []
    longest = 0

    for char in str:
        # if char already exists in substr
        if char in substr:
            # gets index of the first occurence of char
            index = substr.index(char)
            # updates substr to start after the first occurence (Ex. abcade results in abc as substr, but updating substr to start at b
            # means the biggest substr can be bcade)
            substr = substr[index + 1:]
        # adds char to substr
        substr.append(char)
        # checks if current substr length is more than longest, and updates longest with whichever value is higher
        longest = max(longest, len(substr))

    # returns length of longest substring
    return longest

print(length_of_longest_substring("abcabcbb"))  # Should return 3 (substring "abc")
print(length_of_longest_substring("bbbbb"))  # Should return 1 (substring "b")
print(length_of_longest_substring("pwwkew"))  # Should return 3 (substring "wke")