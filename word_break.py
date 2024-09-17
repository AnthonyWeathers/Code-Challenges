"""
Write a function `word_break(s, word_dict)` that takes a string `s` and a dictionary `word_dict` containing a list of words, and 
determines if the string `s` can be segmented into a space-separated sequence of one or more dictionary words.
"""
def word_break(s, word_dict):
    word_set = set(word_dict)  # Convert the list to a set for fast lookups
    dp = [False] * (len(s) + 1)  # Array to store if s[0:i] can be segmented
    dp[0] = True  # Base case: empty string can be segmented
    
    # Iterate over the string
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:  # Check if s[j:i] is a valid word
                dp[i] = True
                break  # No need to check further if we've found a valid segmentation
    
    # Return True if the entire string can be segmented otherwise it will return false
    return dp[len(s)]

print(word_break("leetcode", ["leet", "code"]))  # Should return True
print(word_break("applepenapple", ["apple", "pen"]))  # Should return True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Should return False
