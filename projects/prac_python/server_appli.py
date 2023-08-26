
#Personal Python Playground

import random

print("Hello, Welcome to the beta test of the new server! ")
name = input("Please Enter Your Name : ")
age = int(input("Please Enter Your Age : "))

a = random.randint(1,100)


if age <= 16:
    print("Sorry not eligible")
elif age > 100:
    print("Bro what?")
else:
    print('You are eligible')
    print("Here is your Server Number : ", a)










