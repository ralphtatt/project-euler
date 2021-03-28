"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def is_prime(num: int, primes: list[int]) -> bool:
    # This is assuming the list 'primes' contains all lower valued prime numbers
    for i in primes:
        if num % i == 0:
            return False
    return True

def find_prime(position: int) -> int:
    if position < 1:
        raise Exception()

    primes = [2]
    candidate = 3
    while len(primes) < position:
        if is_prime(candidate, primes):
            primes.append(candidate)
        candidate += 2

    return primes[-1]

prime = find_prime(10001)

print(f"{prime=}")
        



