#simple calculator

# a1 = int(input("Enter the first number:"))
# a2 = int(input("Enter the second number:"))
# add = a1 + a2
# sub = a1 - a2
# mul = a1 * a2
# div = a1 / a2
# mod = a1 % a2
# print("Addition",add)
# print("Subtraction",sub)
# print("Multiplication",mul)
# print("Division",div)
# print("Modulous",mod)
#

#using if condition

print("Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulous")

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
ch = int(input("Enter choice:"))
if(ch==1):
    print("sum",n1+n2)
elif(ch==2):
    print("subtraction",n1-n2)
elif(ch==3):
    print("product",n1*n2)
elif(ch==4):
    print("quotient",n1/n2)
elif(ch==5):
    print("modulous",n1%n2)
else:
    print("invalid")