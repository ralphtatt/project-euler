"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

# This one can definately be improved, but it's quick enough anyway

def is_palindrome(num: int) -> bool:
    num_str = str(num)
    return num_str == num_str[::-1]

largest = -1
for i in range(999,0,-1):
    for j in range(999,0,-1):
        candidate = i * j
        if is_palindrome(candidate):
            if largest < candidate:
                largest = candidate

print(f"{largest=}")
        
