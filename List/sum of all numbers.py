"""
Q. Write a python program to find the sum of all numbers in a list.
"""
# list1 = input("Enter the numbers : ").split()
# # print(list1)
# list2 = []
# for i in list1:
#     list2.append(int(i))
# print(list2)
# sum = 0
# for i in list2:
#     sum = sum + i
# print(sum)

list1 = int(input("Enter the numbers : "))

sum = 0
for i in list1:
    sum = sum + i
print(list(sum))
