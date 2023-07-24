"""Q1. Program to print dictionary,the value is square of key. """

# num = int(input("Enter the number : "))
# dict1 = {}
#
# for i in range(1,num+1):
#     dict1[i] = i * i
#
# print("Square of key : ",dict1)


"""Q2. Take input as sentence and count letters and numbers. """

# a = input("Sentence : ")
# c1 = 0
# c2 = 0
# for i in a:
#     if i.isalpha():
#         c1 += 1
#     else:
#         if i.isdigit():
#             c2 += 1
# print(f'number of char {c1} and number of digit is {c2}')





"""Q3.Python program to find sum and product the items in a dictionary.   """
# dict1 = {"a":10,"b":20,"c":30}
# s = 0
# p = 1
# x = dict1.values()
# for i in x:
#     s = s + i
#     p = p * i
# print(f'Sum of values = {s}')
# print(f'Product of values = {p}')



"""Q4.Sort the list according to length of the strings. """






"""Q5. Check whether a number is perfect number or not."""

# num = int(input("Enter the number : "))
# sum = 0
# for i in range(1,num):
#    if(num % i == 0):
#       sum = sum + i
# if (sum == num):
#    print("The number is a perfect number")
# else:
#    print("The number is not a perfect number")


"""Q6.Write a python program to get a string made of the first 2 and last 2 character of a given strings.  """
s = str(input("Enter the string : "))
l = len(s)
for i in s:
    s2 = s[0:2]+s[-2:]
if l >= 2:
    print("new string : ",s2)
else:
    print("empty string")




"""Q9. Write a python program to find numbers between 100 and 400."""

# items = []
# for i in range(100, 401):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
#         items.append(s)
# print( ",".join(items))
# #


"""Q10. Find median of 3 numbers using list."""

# num = []
# print("Enter the elements")
# for i in range(4):
#     a = int(input("enter the numbers : "))
#     num.append(a)
# print("original list ",num)
# num.sort()
# print("sorted list",num)
# print("median is ",num[1])


"""Q11. Count number of digits in an integer using while loop."""
# num = int(input("Enter the numbers : "))
# count = 0
#
# while num > 0:
#     num //= 10
#     count += 1
#
# print("Number of digits: " + str(count))

