# Python Program to find the factors of a number

def print_factors(x):
   print("The factors of",x,"are")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 250

print_factors(num)