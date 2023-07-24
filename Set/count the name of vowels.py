"""
Q1. Python program to count the name of vowels present in a string using sets.
"""

s = input("Enter string : ")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:",count)


