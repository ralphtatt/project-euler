"""
Problem 17:

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

# String dictionairy for converting from number to text
number_to_string = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    1000 : "onethousand" # Doing this for simplicity
}

# Converts number into parts e.g 73 -> [70, 3]
def deconstruct_number(number: int):
    number = str(number)
    if len(number) == 2:
        return [int(number[0]) * 10, int(number[1])]
    if len(number) == 3:
        return [int(number[0]), int(number[1]) * 10, int(number[2])] # Realised doesn't work for hundreds, still can work


def convert_number_to_string(number: int):
    if number < 21 or number == 1000:
        return number_to_string[number]
    
    num_parts = deconstruct_number(number)
    
    if number < 100:
        return number_to_string[num_parts[0]] + number_to_string[num_parts[1]]
    
    if number < 1000:
        second_part = convert_number_to_string(sum(num_parts[1:]))
        if len(second_part) == 0:
            return number_to_string[num_parts[0]] + "hundred"
        return number_to_string[num_parts[0]] + "hundred" + "and" + second_part

LIMIT = 1000

total_characters = sum([len(convert_number_to_string(i)) for i in range(1, LIMIT+1)])

print(f"{total_characters=}")