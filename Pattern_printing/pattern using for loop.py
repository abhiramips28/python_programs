#Q.try to create diamond pattern using for loop.

# rows = int(input("Enter a number : "))
# for i in range(rows+1):
#     for m in range(rows-i):
#         print(" ",end=" ")
#     for n in range(i+1):
#         print("*  ",end=" ")
#     print()
# for j in range(rows,0,-1):
#     for o in range(rows-j+1):
#         print(" ",end=" ")
#     for p in range(j):
#         print("*  ",end=" ")
#     print()


#Q.try to create below designed pattern.

rows = int(input("Enter a number : "))
for j in range(rows,0,-1):
    for o in range(rows - j):
        print(" ",end=" ")
    for p in range(j):
        print("*  ",end=" ")
    print()
for i in range(rows):
    for m in range(rows-i-1):
        print(" ",end=" ")
    for n in range(i+1):
        print("*  ",end=" ")
    print()
