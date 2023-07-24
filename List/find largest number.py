"""
Q. Write a python program to find largest number in a given list without using max()
"""

list1 = input("Enter the numbers : ").split()
list2 = []
for i in list1:
    list2.append(int(i))
print(list2)
s = sorted(list2)
print(s)
print("The largest number is : ",s[-1])




#
# l = list(map(int(input("Enter array elements:").split(" "))))
# max1 = l[0]
# for i in range(1, len(l)):
#     if (l[i] > max1):
#         max1 = l[i]
# print(max1)
