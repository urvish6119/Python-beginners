# Python is same as any other language, requires quotes to define strings and nothing for numberes.
# For example after installing python, open python IDEL and type 2 and press enter, It will simply print the 2
# The following line will print the integer 5 if type in IDLE
5
# following line will print integer 5 in IDLE.
int('5')
# following line will print integer 5 in IDLE.
int(5)
# print function using variable.
x=5
print(x)
# you can assign multiple values in same line to multiple variables.
x, y, z = 5, 6, 7
print("X=",x,"y=",y ,"z=",z)
# Integers means any value either negative or positive
x ,y = -5, 5
print("x=",x,"y=",y)
# It updates the value if used same variable again and again
x=10
print("x=",x)
x=20
print("x=",x)
x=30
print("x=",x)
#------------------------------------------------------------------------------------------------------------------------------#
# Now let's use string, following line will simply print the 'John' in IDLE
'John'
# Following line will also print the same as above, ofcourse in Idle
"John"
# The following line will print the string 5 if type in IDLE
'5'
# or
"5"
# following line will print string 5 in IDLE.
str('5')
# following line will print string 5 in IDLE.
str("5")
# following line will print string 5 in IDLE.
str(5)
# print function using variable to print string.
x='5'
print(x)
# or
x="5"
print(x)
# you can assign multiple values in same line to multiple variables.
x, y, z = 'abc', 'xyz', 'pqr'
print("X=",x,"y=",y ,"z=",z)
#------------------------------------------------------------------------------------------------------------------------------#
# Now let's try some float numbers.
# following line is for using in IDLE, it will pint 5.632
x=5.632
x
# it is same as using integers, you just get to use floating numbers, that's the onlu differance.
# Following line will print simple x=5.632
x=5.632
print("x=",x)
#------------------------------------------------------------------------------------------------------------------------------#
# There is a function called round to use with the floating point numbers.
# for example following lines will be give output 26, 30 respectively.
x=25.69
print(round(x))
x=30.49
print(round(x))
# As we can see in above example, it took upcoming number if the value after . is bigger then 50 and it took same number if less then 50
# So what if the number is exact 50?
# It will take the number as same, it won't take the next number.
x=40.50
print(round(x))
# There is one more functionality in round function, let's see the example
# following example will print 32.56 only and remove and take the upcoming or the downgoing number.
# in first it will remove 78 and change 6 to 7, as 678 is bigger then 500
# in second it will remove 678 and change 5 to 6, as 5678 is bigger then 5000
x=32.5678
print(round(x,2))
print(round(x,1))
# same applies for the number with only 5 at last, it will take only 5 and does nothing because the given condition is for after decimal point.
x=32.500
print(round(x,2))
# same function can be used with negative marking as well to remove the number after decimal point.
# in given example it will give output of 30, not 32 because in condition we remove the values after decimal points and round value after decimal points.
x=32.5678
print(round(x,-1))
# round function with negative values can be used on integer values as well.
#------------------------------------------------------------------------------------------------------------------------------#
# Now to understand it batter there is a function known as "type" in python.
# to try in IDLE
# following line will give output <class 'int'>
type(5)
# following line will give output <class 'str'>
type('5')
# following line will give output <class 'str'>
type("5")
# following line will give output <class 'int'>
type(5+5)
# following line will give output <class 'str'>
type('5'+'5')
# following line will give output <class 'int'>
type(int(5)+int('5'))
# following line will give output <class 'str'>
type(str(5)+str('5'))
# how to call integer in print statement
x=10
print(x)
# or gives output <class 'int'>
x=10
print("value of x = ", x ," and type =",type(x))
# how to call string in print statement
x='10'
print(x)
# or gives output <class 'str'>
x='10'
print("value of x = ", x ," and type =",type(x))
#------------------------------------------------------------------------------------------------------------------------------#
# Another function known as "del" to delete the variable assign value.
x=10
print(x)
del x
print(x)
# following line will print no output as x is already deleted.
print(x)
# same function apply for string as well.