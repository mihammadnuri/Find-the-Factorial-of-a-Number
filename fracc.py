                    
import math

n = int (input (“Enter the number whose factorial you want to find: ”))

print (“The factorial of the number is: “)

print (math.factorial (n))
n = int (input (“Enter a number: “))

factorial = 1

if n >= 1:

              for i in range (1, n+1):

                             factorial = factorial *i

print (“Factorial of the given number is: “, factorial)

n = int (input (“Enter the number for which the factorial needs to be calculated: “)

factorial = 1

if n < 0:

              print (“Factorial cannot be calculated, non-integer input”)

elif n == 0:

              print (“Factorial of the number is 1”)

else:

              for i in range (1, n+1):

                             factorial = factorial *i

              print (“Factorial of the given number is: “, factorial)

n = int (input (“Enter the number for which the factorial needs to be calculated: “)

def rec_fact (n):

              if n == 1:

                             return n

elif n < 1:

              return (“Wrong input”)

else:

              return n*rec_fact (n-1)

print (rec_fact (n))
