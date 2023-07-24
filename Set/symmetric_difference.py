# Q9. Write a python program to create a symmetric difference.


set1 = {"a","b","c",1,2,"anvi"}
set2 = {1,5,9,7,"a","b",10,22,"m"}
# z = set1.union(set2)
# print(z)
set1.symmetric_difference_update(set2)
print(set1)