"""
Q. Write a Python program to reverse a string.
        Sample String: "1234abcd"
        Expected Output: "dcba4321"
"""
# def reverse_string(r):
#     x = (r[::-1])
#     print(x)
# r = input("enter the string : ")
# reverse_string(r)

# Print Pascal's Triangle in Python , anaga
from math import factorial

# input n
n = 5
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    # for new line
    print()