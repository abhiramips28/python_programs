'''Q. Factorial of a number.'''

def factorial(n):
    if n < 0:
        return f'number should be 0 or higher'
    def inner_factorial():
        prod = 1
        for i in range(1,n+1):
            prod *= i
        return prod
    return inner_factorial()
print(factorial(5))