#Q1. WAP prgm to check whether a number is prime or not...?

n = int(input("Enter a number :"))
if n>1:
  for i in range(2,n):
     if (n%i)==0:
        print(n,"is not a prime number")
        break
  else:
    print(n,"is a prime number")
else:
    print(n,"is not prime number")


# n = input(input("Enter a number:"))
# c=0
# if i in range(1,n+1)
#

#Q2. WAP prgm to display product of the digits of a number accpted from the user.

# n = int(input("Enter a number : "))
# p = 1
# for i in range(0,n+1):
#   d = n%10
#   p = p*d
#   n = n//10
#   print("d = ",d)
#   print("n = ",n)
#   print("p = ",p)
#   if n==0:
#     break
# print("product of the value: ",p)


#another method

# n = int(input("Enter a number : "))
# num = str(n)
# prod = 1
# for i in num:
#   prod = prod * int(i)
# print("Product : ",prod)
#


#Q3. Accept 10 numbers from the user and display their average.

# t_sum = 0
# for i in range(10):
#   n = float(input("Enter a number : "))
#   t_sum += n
# avg = t_sum/10
# print("The average of these numbers is : ",avg)



#Q4. WAP prgm to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

# for i in range(100,501):
#   if i%11 == 0 and i%2 != 0 :
#      print(i,end=" ")
#

