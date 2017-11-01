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
# following line will print no output as x is already deleted.
print(x)
# same function apply for string as well.