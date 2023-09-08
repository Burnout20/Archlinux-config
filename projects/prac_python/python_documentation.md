

# This is Where I will be Writing down all the important factors that need to 
# be rememberd about python 


 you can commpress the output of a statement into a certain data type 
 by doing  

```python

age = int(input("What is youe age : "))
print(age)

```  

 what i have done above is that i've commpressed the answer to a interger form by
 adding it at the end 

    
 ## if statements     

```python

age = int(input("What is your age "))


if age <= 16:
    print("Too Young")
elif age > 100: #Make sure to always add the condition on the elif statement  
    print("Bro ??")
else:
    print("You can go ")

```

 pretty much every basic idea about if conditions 

 nested statements and chained conditions are advanced concepts of if 
 statements

```python

x = 2 
y = 3 s

if x == 2:
    if y == 3:
        print("x is 2 and y is 3 ")
    else:
        print("x is 2 and y is not 3 ")
else:
    print("x is not 2 ")


```
 chained conditions basically says that you can add any amount of if statements within 
 eachother (This is whats shown above). And the fact that if one condition is  true 
 it moves on to the next for ex :- in the above example if x = 2 then it moves on to 
 see if y = 3 if so it prints the 1st statement and if y != 3 then it moves on to the 
 else statement and if the 1st statement is not true it ingnores the rest and moves on 
 to the main else statement



 nested statements are like logic gate statements, where they are used on the sence
 that if `and` is shown both statements have to be true, if `or ` is shown then 
 one of the conditions have to be true and finally the `not` statement makes it 
 so that the answer to the condition is flipped 

```python

 x = 2 
 y = 3 

 if x == 2 and y == 3:
     print("Yes sir ")
 else:
     print("Even Better")


```

```python

 x = 2 
 y = 3 

 if x == 2 or y == 4:
     print("Whats up")
 else:
     print("Too Bad")


```

 in the above instance it doesn't matter that one statement is false since 
 the condition is `or`


```python



 x = 2 
 y = 3 


 if not (x == 2 or y == 3):
     print ("True")
 else:
     print(":(")

```

 In the above instance the answer is flipped because the condition is not
 so if the condition inside the bracktes is `or ` or `and ` the output that 
 is recived from that bracket is the opposite of it so if x = 2 and y = 3  
 the answer from the bracket would be true but it's false at the end because
 of the `not` condition (Run the above code for more understanding)


 ## Loops  

 There are 2 types of loops, for loops and while loops. Both can be used in different
 instances. We will start by lokking at for loops 
 
 ```python

 for x in range (0,200,1):
     print(x)
 

 ```
 This is a basic `for ` loop. The keywords are for, in and range and the 
 content in the brakets are used to tell the starting postiton (first 1)
 the range which means for how long it should print the numbers or you can 
 simply call it the ending postiton, and finally the step amount, in this 
 example the step amount is 1 which means that the numbers will move from 
 one to one (1,2,3,4) if the number was 2 then (2,4,6,8) likewise 


 Next are While Loops 

 ```python
 
 



 ```


 When Using Lists you can choose a specific element by selecting the number of it (0,1,2)

```python

fruits = ["apples ", "oranges", "pears"]
print(fruits[1])
fruits.append("strawberry")
print(fruits)
fruits[1]="blueberry"
print(fruits)

```








