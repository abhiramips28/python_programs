#Q. Try to create hollow diamond pattern
#
# num = int(input("Enter a number : "))
# for i in range(0,num):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         if k == 0 or k == i:
#             print("* ",end="  ")
#         else:
#             print("  ",end="  ")
#     print()
# for p in range(0,num-1):
#     for q in range(0,p+1):
#         print(" ",end= " ")
#     for r in range(0, num-p):
#         if r == 0 or r == num-p-2:
#             print("* ",end="  ")
#         else:
#             print("  ",end="  ")
#     print()


#Q. Reverse number pattern from 10 to 1.

#
# rows = 10
# for i in range(0, rows + 1):
#     for j in range(rows - i, 0,-1):
#         print(j, end=" ")
#     print()
#


#Q. Square pattern - alphabet

rows = int(input("Enter a number :"))
A = 65
for i in range(rows):
     for j in range(rows):
        print(chr(A)," ",end = " ")
        A=A+1
     print()