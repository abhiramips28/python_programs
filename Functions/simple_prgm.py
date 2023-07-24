""" Q.3	Write a Python function to calculate the factorial of a number (a non-negative integer).
         The function accepts the number as an argument. """

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     return fact
# n = int(input("enter the numbers: "))
# print(f"factorial is {factorial(n)}")





"""Q4.Write a Python function that takes a number as a parameter and check  the number is prime or not."""

# def prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime number")
# n = int(input("Enter the number: "))
# prime(n)
#



"""Q.Generate a Python list of all the even numbers between 4 to 30. """

def even(num):
    for i in range(4,30):
        if i % 2 == 0:
            list.append(i)
    print(list)
list = []
even(list)