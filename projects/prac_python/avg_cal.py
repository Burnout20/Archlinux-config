# Getting the inputs from users

sub1 = int(input("How much marks for the 1st Subject : "))
sub2 = int(input("How much marks for the 2nd Subject : "))
sub3 = int(input("How much marks for the 3rd Subject : "))
sub4 = int(input("How much marks for the 4th Subject : "))
sub5 = int(input("How much marks for the 5th Subject : "))


# calculating total
tot = sub1 + sub2 + sub3 + sub4 + sub5
print("Your Total is : ", tot)


# calculating avarage
avg = tot / 5
print("Your Avarage is : ", avg)
