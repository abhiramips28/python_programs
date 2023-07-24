"""Q6. Write a python program to create a list of even numbers and
           another list of odd numbers from a given list. """
list1 = input("Enter the numbers : ").split()
list2 = []
for i in list1:
    list2.append(int(i))
print(list2)
evenlist = [ ]
oddlist = [ ]
for i in list2:
    if int(i) % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("Even numbers are = ",evenlist)
print("Odd numbers are = ",oddlist)
