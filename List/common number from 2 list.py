"""
Q. Write a python program to find the common numbers from two lists
"""
list1 = input("Enter the 1st numbers : ").split()
l1 = []
for i in list1:
    l1.append(int(i))
print("1st list : ",l1)

list2 = input("Enter the 2nd numbers : ").split()
l2 = []
for i in list2:
    l2.append(int(i))
print("2nd list : ",l2)

c = 0
print("common numbers are")
for i in l1:
    for j in l2:
        if i == j:
          if c == 0:
            print(i,end = ' ')
          else:
            print(i,end = ' ')
          c = c + 1
          break
