
import random 

print("Welcome to the Beta Testing of a python application")
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

a = random.randint(1,300)

if age < 16:
    print("Too Young To Enter ")
elif age > 100:
    print("Bro ??") 
else:
    print("You are accepted ")
    print("Here is your id Number : ",a)


