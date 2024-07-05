def sum_of_evens(numbers):
    # numbers is the array of numbers passed in
    sum = 0 # sum is initialized to 0
    for num in numbers: # loops through each element of list
        if num % 2 == 0: # checks if current element is is divisible by 2
            sum += num # adds the element's value if divisible by 2, indicating its an even number
    print(sum) # prints the sum

sum_of_evens([1, 2, 3, 4, 5, 6])  # Should return 12 (2 + 4 + 6)
sum_of_evens([7, 8, 10, 13, 17, 19])  # Should return 18 (8 + 10)