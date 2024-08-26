"""
Write a function `product_except_self(nums)` that takes a list of integers `nums` and returns a list such that each element at index 
`i` is the product of all the numbers in the original array except the one at `i`.
"""

def product_except_self(nums):
    products = []

    for num in nums:
        # reset product to 1
        product = 1
        for num2 in nums:
            # if state is to ensure the product is of all integers except the one at index i, represented as num
            if num == num2:
                continue
            else:
                product *= num2
        products.append(product)
    return products

print(product_except_self([1, 2, 3, 4]))  # Should return [24, 12, 8, 6]
print(product_except_self([2, 3, 4, 5]))  # Should return [60, 40, 30, 24]
