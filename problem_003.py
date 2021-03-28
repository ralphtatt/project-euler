"""
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import math

def largest_prime_factor(num: int) -> int:
    if num < 2:
        raise Exception("Stop imagining things")

    # Special case for 2
    while num % 2 == 0:
        max_prime = 2
        num /= 2

    # Odd numbers
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            max_prime = i
            num /= i

    if num > 2:
        max_prime = num

    return max_prime

largest_factor = largest_prime_factor(600851475143)
print(f"{largest_factor=}")

