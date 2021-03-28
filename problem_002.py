"""
Problem 2:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""

# I don't have much experience with yields!
def calculate_next_fibonacci_number():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

sequence = calculate_next_fibonacci_number()

LIMIT = 4000000
total = 0
for i in sequence:
    if i > LIMIT:
        break
    if i % 2 == 0:
        total+= i

print(f"{total=}")