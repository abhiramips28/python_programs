"""
Q. Write a python program to print all even numbers from a given list.
"""
list1 = input("Enter the numbers : ").split()
list2 = []
for i in list1:
    list2.append(int(i))
print("Numbers : ",list2)
print("Even numbers are")
for i in list2:
    if i % 2 == 0:
        print(i,end = ',')