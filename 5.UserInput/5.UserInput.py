# There is a function known as input to take a input from user while program is running,
# Exapmle:
print('Enter anything:')
x=input()
print('You enterd:',x)
print('Type:',type(x))
# here no matter if you enter number it will take it as string, to tale input as number you have to define the input type.
print('Enter int 1:')
x=input()
print('Enter int 2:')
y=input()
num1=int(x)
num2=int(y)
print(num1,'+',num2,'=',num1+num2)
print(type(num1))
print(type(num2))
# Thre is one more way to write this same program in another way using less lines.
num1= int(input('Enter int 1:'))
num2= int(input('Enter int 2:'))
print(num1,'+',num2,'=',num1+num2)
print(type(num1),'\n',type(num2))
# You can use string or float in place of int.