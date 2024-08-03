"""
Write a function is_valid(s) that takes a string s containing just the characters '(', ')', '{', '}', '[' and ']', and 
determines if the input string is valid. An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

def is_valid(s):
    stack = []
    # A dictionary to hold the matching pairs of the opening to closing parentheses
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_brackets.values():  # If char is one of the opening pairs: '(', '{', '[', then 
            # it would be added to the stack to track the order of parentheses
            stack.append(char)
        elif char in matching_brackets.keys():  # If char is one of the closing pairs ')', '}', ']' then
            # check if the stack is empty or the top of the stack is not the matching opening pair
            if stack == [] or stack.pop() != matching_brackets[char]: # if either is true then it is not
                # a valid string of parentheses
                return False
        else:
            # If the input has an invalid character not in the matching_brackets
            return False
    
    return stack == []  # Returns true if the stack is empty indicating that input was a valid string of parentheses

print(is_valid("()"))  # Should return True
print(is_valid("()[]{}"))  # Should return True
print(is_valid("(]"))  # Should return False
print(is_valid("([)]"))  # Should return False
print(is_valid("{[]}"))  # Should return True
print(is_valid("{({[]})}"))  # Should return True
print(is_valid("{}[{(]})"))  # Should return False