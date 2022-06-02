#!/usr/bin

try:
     num = int(input("Enter a number between 100 and 999: "))
except ValueError:
     num = 0
print(num)
if num < 100 or num > 999:
     print("The number must be between 100 and 999")
else:
     x = num 
     digits = []
     while x != 0:
         digit = x % 10
         digits.append(digit)
         x = int(x/10)
     sum = 0
     for i in digits:
         sum = sum + (i ** len(digits))
     if sum == num:
         print("Narcissistic Number")
     else:
         print("Not Narcissistic Number")


    
        






    
