"""
Problem 10:


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Notes:

This one is slow, could definately be improved
"""

import time

def is_prime(num: int, primes: list[int]) -> bool:
    # This is assuming the list 'primes' contains all lower valued prime numbers
    for i in primes:
        if num % i == 0:
            return False
    return True

def find_primes_below_value(position: int) -> int:
    if position < 1:
        raise Exception()

    primes = [2]
    candidate = 3
    while primes[-1] < position:
        if is_prime(candidate, primes):
            primes.append(candidate)
        candidate += 2
        if candidate > position:
            break

    return primes

start_time = time.time()

LIMIT = 2000000
total = sum(find_primes_below_value(LIMIT))

time = time.time() - start_time

print(f"{total=}") 
print(f"{time=}") 

