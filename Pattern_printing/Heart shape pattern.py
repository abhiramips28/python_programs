#Q. To print Heart Shape Pattern.

num = int(input("Enter a number : "))
n = num//2

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")

    if num%2 == 0:
        for x in range(2*(n-i-1)):
            print(" ",end="")
    else:
        for x in range(2*(n-i-1)+1):
            print(" ",end="")

    for m in range(i+1):
        print("* ",end="")
    print()

for i in range(num,0,-1):
        for o in range(num - i):
            print(" ",end="")
        for p in range(i,0,-1):
            print("* ",end="")
        print()