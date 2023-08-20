# # Write a Python program that accepts an integer (n) and computes the value
# # of n+nn+nnn + …

x=int(input("enter a number"))#3
sec=x*10
thrid=x*100
print(sec)
print(thrid)
print(x+sec+thrid)

for i in range(0,x):
   print(i)
#3+33+333


# Write a Python program to calculate the difference between a given
# number and 17. If the number is greater than 17, return twice the absolute
# difference.
x=int(input("enter a number"))
if x > 17:
   print(2 * abs(x-17))
else:
   print(x-17)
#Write a Python program to check whether the input number is prime or not.

x=int(input("enter a number"))

if x % 2:
   print("prime")
else:
   print("not prime")



