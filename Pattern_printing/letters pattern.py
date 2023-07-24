#Q. To print the character of first letter of your name.


for rows in range(0,7):
    for col in range(0,5):
        if (col == 0 or col == 4)  or (rows == 0 or rows == 3):                                                    #and (col > 0 and col < 4)):
            print("* ",end="")
        else:
            print(end="  ")
    print()







# H - star pattern.

# n = int(input("Enter the name : "))
# for i in range(n):
#     for j in range(n-2):
#         if j==0 or j==(n-3) or  i == n//2 and (j>0 and j<(n-3)):
#             print("* ",end=" ")
#         else:
#             print(end="")
#     print()