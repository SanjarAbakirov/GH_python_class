#  discrete math in Python iteration
# Number Theory: Python can handle large integers and perform modular arithmetic, useful for
# problems involving prime numbers, divisibility, and cryptography.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(17))  # True

# Problem. Is there a positive integer that is divisible by  and ends with ?

# To prove that such a number exists, it is enough to give a single example.
# One such example is : it ends with  and it is divisible by  ().
# This already proves the existence, and we don't even need to explain how we have found this integer.
# Still, the following three lines of code help to find all such integers in the range .


for n in range(10 ** 4):
    if n % 13 == 0 and n % 100 == 15:
        print(n)

# This program checks all numbers in .
# Here,  stands for . In ,  where  is some non-negative number is a list (sequence) of  numbers .
# The  loop goes over all of them in this order; the  operator checks whether they have the required properties.
# The last two digits of an integer  can be computed as . In general,  denotes the remainder when dividing  by .
# (Imagine we have identical books on the table and pack them into boxes that contain  books each.
# Then  books remain unpacked.)
