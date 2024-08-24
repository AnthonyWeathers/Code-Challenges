"""
Write a function generate_squares(n) that takes a positive integer n and returns a list of the squares of numbers from 1 to n.
"""

def generate_squares(n):
    squares = []
    # loops through from 0 up to the input number n
    for num in range(n):
        # adds 1 since range is 0 to n - 1, to get 1 to n
        squares.append(pow(num + 1, 2)) # uses the pow function on num + 1, to obtain the square number and adds it to the new list
    return squares

print(generate_squares(5))  # Should return [1, 4, 9, 16, 25]
print(generate_squares(3))  # Should return [1, 4, 9]
print(generate_squares(8))  # Should return [1, 4, 9, 16, 25, 36, 49, 64]