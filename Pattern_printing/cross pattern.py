#cross pattern.

rows = int(input("enter a number : "))
for i in range(0, rows):
    for j in range(0, rows):
        if i == j or j == rows - 1 - i:
            print("* ",end =" ")
        else:
            print("  ", end =" ")
    print()



#number cross pattern.

# n = int(input("enter a number : "))
# for i in range(0, n):
#     for j in range(0,n+1):
#         if i == j or j == n - 1 - i:
#             print(i,end =" ")
#         else:
#             print("  ", end =" ")
#     print()



#Q. Cross number pattern.
#
# rows = int(input("Enter a number : "))
# for i in range(rows,0,-1):
#     for k in range(rows-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         if j == 1 or j == i:
#            print(rows-i+1,end=" ")
#         else:
#            print("   ",end=" ")
#     print()
# for i in range(1,rows):
#     for k in range(rows-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         if j == 0 or j == i:
#             print(rows-i,end=" ")
#         else:
#             print("  ",end=" ")
#     print()
#
#


#Another method
"""
1   5
 2 4
  3
 2 4
1   5 
"""
# num = input("Enter a number:")
# length = len(num)
# for i in range(length):
#     for j in range(length):
#         if i == j or i+j == length-1:
#             print(num[j],end= " ")
#         else:
#             print(" ",end= " ")
#     print()