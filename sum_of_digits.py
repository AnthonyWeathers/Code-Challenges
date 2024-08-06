"""
Write a function `sum_of_digits(n)` that takes a non-negative integer `n` and returns the sum of its digits.
"""

def sum_of_digits(n):
    n = str(n)
    sum = 0
    for num in n:
        sum += int(num)
    return sum

print(sum_of_digits(123))  # Should return 6 (1 + 2 + 3)
print(sum_of_digits(456))  # Should return 15 (4 + 5 + 6)
print(sum_of_digits(42))  # Should return 6 (4 + 2)
print(sum_of_digits(7549))  # Should return 25 (7 + 5 + 4 + 9)