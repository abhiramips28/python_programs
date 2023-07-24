"""
Q1. Remove special symbols/puntuation from strings.
     str1 = "/*Jon is 2developer & music director
     o/p = Jon is developer music director
"""

# a = input("Enter the strings : ")
# b = ""
# for i in a:
#     if i.isalpha() == True or i.isspace() == True:
#         #print(i)
#          b += i
# print("Result : ",b)

"""
Q2. To find if two strings are anagrams or not.

"""
# a = input("Enter the strings : ")
# b = input("Enter the strings : ")
# if len(a) == len(b):
#     if sorted(a) == sorted(b):
#         print("Given strings are anagram.")
#     else:
#         print("Given strings are not anagram.")
# else:
#     print("Given strings are not anagram.")


"""
Q3. To calculate the length of a string without using a library function.
"""
# str1 = input("Enter the strings : ")
# i = 0
# for x in str1:
#     i += 1
# print("The length of the string is ",i)

"""
Q4. To check if a string is palindrome or not.
"""
# string = input("Enter a strings : ")
# if(string == string[::-1]):
#     print("The string is a palindrome.")
# else:
#     print("Not a palindrome.")


# Program to check if a string is palindrome or not

# my_str = 'aIbohPhoBiA'
#
# # make it suitable for caseless comparison
# my_str = my_str.casefold()
#
# # reverse the string
# rev_str = reversed(my_str)
#
# # check if the string is equal to its reverse
# if list(my_str) == list(rev_str):
#    print("The string is a palindrome.")
# else:
#    print("The string is not a palindrome.")

"""
Q5. Write a python code to remove all the repeating letters from a each words of a given sentence.
    eg:-  i/p = Let's google the pineapple
          o/p = Let's gole the pineal
"""
# string1 = input("Enter the strings : ")
# x = ""
# y = ""
# for i in string1.split(" "):
#     for j in i:
#         if x.find(j) == -1:
#             x += j
#         else:
#             continue
#
#     y += x + " "
#     x = ""
# print(y)

#Q5. Another method

# str3 = "Let's google the pineapple"
# str1 = str3.split(' ')
# print(str1)
# str2 = [ ]
# for i in str1:
#     l = " "
#     for j in i:
#        if j in l:
#           continue
#        else:
#            l =  l+j
#
#     str2.append(l)