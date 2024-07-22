"""
Write a function count_vowels(s) that takes a string s and returns the number of vowels in the string.
"""

def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))  # Should return 2
print(count_vowels("Python"))  # Should return 1
print(count_vowels('abracadabra')) # Should return 5
print(count_vowels("HELLO"))  # Should return 2
print(count_vowels("PyThOn"))  # Should return 1