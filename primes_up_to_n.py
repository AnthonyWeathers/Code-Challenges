"""
Write a function `primes_up_to(n)` that takes an integer `n` and returns a list of all prime numbers up to `n`.
"""

def primes_up_to(n):
    # handle case if n is less than 2 indicating no primes possible
    if n < 2:
        return []
    all_primes = []
    # loop starts from 2 as first prime number and goes to n
    for i in range(2, n + 1):
        prime = True
        # loops from 2 upto square root of i + 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        # if i is prime then the number gets added to the list
        if prime:
            all_primes.append(i)
    # print or return the list of all primes up to given n
    print(all_primes)
    # return all_primes

primes_up_to(10)  # Should return [2, 3, 5, 7]
primes_up_to(20)  # Should return [2, 3, 5, 7, 11, 13, 17, 19]