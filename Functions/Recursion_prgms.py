''' Q. Python program to find LCM of two numbers using recursion.'''

def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


def lcm(a, b):
    return (a * b) // hcf(a, b)


first = int(input("enter the 1st number: "))
second = int(input("enter the 2nd number: "))

print("Lcm of", first, "and", second, "is", lcm(first, second))


# def num(num1,num2):
#     if num1 >= num2:
#         if num2 == 0:
#             s = num1 * num2
#         return s
#
# s1 = int(input("enter 1st the number: "))
# s2 = int(input("enter the 2nd number: "))
# print("LCM of given numbers: "+s)
# num(s1,s2)


#
# def lcm(a, b):
#     if b == 0:
#         return a
#     return a * b / lcm(a, b)
#
# print(lcm(5,3))
#






"""Q2. To find product of two numbers using recursion."""



"""Q3. To reverse a string using recursion."""