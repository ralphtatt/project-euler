"""
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def get_triplet(limit: int):
    for a in range(1,limit):
        for b in range(a,limit):
            c = limit - a - b
            if a**2 + b**2 == c**2:
                return [a, b, c]

triplet = get_triplet(1000)
print(triplet)

product = triplet[0] * triplet[1] * triplet[2]
print(f"{product=}")
