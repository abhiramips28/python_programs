'''
 Q10. Write a python program to check if a set is a subset of another set.
'''

x = {"a", "b", "c"}
y = {"e", "f", "g", "c", "b", "a"}
z = x.issubset(y)
print(z)