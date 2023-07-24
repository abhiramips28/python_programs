'''Q. Multiply all the numbers in a list using function.'''


def multiply(m):
    x = 1
    for i in m:
        x = x * i
    print(x)
m = [1,2,3,4,5]
multiply(m)

another method #not
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
numbers = int(input("enter the numbers : "))
# print("multiply all the numbers : "+multiply(numbers))
multiply(numbers)