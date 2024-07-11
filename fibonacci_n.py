"""
Write a function fibonacci(n) that takes an integer n and returns the first n numbers in the Fibonacci sequence.
"""

def fibonacci(n):
    if n == 0:
        # return an empty list
        return []
    elif n == 1:
        # return only 0
        return [0]
    else:
        n1 = 0 # first number of the sequence
        n2 = 1 # second number of the sequence
        nList = [0, 1] # list already holds the first two numbers
        # loops until n, but would exit immediately if n == 2, to return the list of the sequence that would be correct for n = 2 
        for i in range(3, n+1):
            n3 = n1 + n2 # gets the sum of the previous two numbers
            nList.append(n3) # adds the sum to the end of the list/sequence
            # adjusts n1 and n2 so they hold the last two numbers to get the next number for the sequence
            n1 = n2
            n2 = n3

        return nList

print(fibonacci(2)) # should return [0, 1]
print(fibonacci(3)) # should return [0, 1, 1]
print(fibonacci(4)) # should return [0, 1, 1, 2]
print(fibonacci(5)) # should return [0, 1, 1, 2, 3]
print(fibonacci(7))  # Should return [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(10))  # Should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]