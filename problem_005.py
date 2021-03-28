"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Notes on solution:

This is built up iteratively.
Starting at 2, for each subsequent number you add in any prime factors that are not already accounted for.

"""
import math
from collections import defaultdict

def get_prime_factors(num: int) -> list[int]:
    # Dict with default values of 0
    prime_factors = {}
    prime_factors = defaultdict(lambda: 0, prime_factors)
    if num < 2:
        raise Exception("stop imagining things")
    # Special case for 2
    while num % 2 == 0:
        prime_factors[2] += 1
        num /= 2

    # Odd numbers
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            prime_factors[i]+= 1
            num /= i
            num = num 
    
    if num > 2:
        prime_factors[num]+= 1

    return dict(prime_factors) # Convert back to standard dict


def find_minimum_prime_factors_needed(limit: int) -> dict[int, int]:
    prime_factors_needed = {}
    prime_factors_needed = defaultdict(lambda: 0, prime_factors_needed)

    for i in range(2, limit):
        new_prime_factors = get_prime_factors(i)
        for key in new_prime_factors:
            if new_prime_factors[key] > prime_factors_needed[key]:
                prime_factors_needed[key] = new_prime_factors[key]
    return dict(prime_factors_needed)

def calculate_prime_factor_sum(factors: dict[int, int]) -> int:
    total = 1
    for key in factors:
        total *= math.pow(key, factors[key])
    return int(total)


factors = find_minimum_prime_factors_needed(20)
minimum = calculate_prime_factor_sum(factors)
print(f"{minimum=}")
