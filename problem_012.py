"""
Problem 12:

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""

import math


def get_triangle_numbers():
    nth_tri = 1
    while True:
        yield int((nth_tri) * (nth_tri + 1)/ 2)
        nth_tri += 1 


def get_number_of_divisiors(number: int):
    total_divisors = 0
    limit = int(math.sqrt(number))

    for i in range(1, limit):
        if number % i == 0:
            total_divisors += 2
    
    return total_divisors


def get_triangle_number_with_more_divisors_than(divisor_limit: int):
    triangle_numbers = get_triangle_numbers()

    for i in triangle_numbers:
        if get_number_of_divisiors(i) > 500:
            return i


number = get_triangle_number_with_more_divisors_than(500)
print(f"{number=}")
