"""Q7.Write a python program to remove repeated elements from a given list without using built-in methods. """
list_to_remove = ["let's","google","the","pineapple","photos","google","photos"]
list2 = []
for i in list_to_remove:
    if i not in list2:
       list2.append(i)
print(list2)
