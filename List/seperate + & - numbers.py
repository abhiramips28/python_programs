"""
Q. Write a program to separate negative and positive numbers from a given list ? (accept input from the user.)
"""
list1 = int(input("Enter the numbers : "))
list2 = []
for i in list1:
    list2.append(i)
    print(list2)
positive = []
negative = []
for i in list2:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
print("Positive numbers = ",positive)
print("Negative numbers = ",negative)
