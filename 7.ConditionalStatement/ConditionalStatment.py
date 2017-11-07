# let's try simple if statement:
divident=int(input("please enter divident:"))
diviser=int(input("please enter diviser:"))
if diviser != 0:
    print(divident ,'/',diviser ,'=', divident/diviser )
else:
    print("didnot enter valid diviser.")
# compounded boolean expression:
# and, or, not
x=10
y=20
if x==10 and y==20:
    print('True')
if x==10 or y==10:
    print('True')
if not (x == y):
    print('True')
# There is pass statement as well, which will do nothing and pass the condition.
# for example:
x=20
if (x/2):
    print('Divisible')
if (x/4):
    print('Divisible')
if (x/5):
    pass
if (x/10):
    print('Divisible')
# nested if conditions:
x = int (input('enter number:'))
if x>=0:
    if x<=10:
        print('number is in 1 to 10')
    else:
        print('number is big then 10')
else:
    print(x,'is too small')
# multiway decision statement:
value = int(input("Please enter an integer in the range 0...5: "))
if value < 0:
    print("Too small")
else:
    if value == 0:
        print("zero")
    else:
        if value == 1:
            print("one")
        else:
            if value == 2:
                print("two")
            else:
                if value == 3:
                    print("three")
                else:
                    if value == 4:
                        print("four")
                    else:
                        if value == 5:
                            print("five")
                        else:
                            print("Too large")
print("Done")
# elif condition for multiple conditions:
month = int(input("Please enter the month as a number (1-12): "))
day = int(input("Please enter the day of the month: "))
# Translate month into English
if month == 1:
    print("January ", end='')
elif month == 2:
    print("February ", end='')
elif month == 3:
    print("March ", end='')
elif month == 4:
    print("April ", end='')
elif month == 5:
    print("May ", end='')
elif month == 6:
    print("June ", end='')
elif month == 7:
    print("July ", end='')
elif month == 8:
    print("August ", end='')
elif month == 9:
    print("September ", end='')
elif month == 10:
    print("October ", end='')
elif month == 11:
    print("November ", end='')
else:
    print("December ", end='')
# Add the day
print(day, 'or', day, end='')
# Translate month into Spanish
if month == 1:
    print(" de enero")
elif month == 2:
    print(" de febrero")
elif month == 3:
    print(" de marzo")
elif month == 4:
    print(" de abril")
elif month == 5:
    print(" de mayo")
elif month == 6:
    print(" de junio")
elif month == 7:
    print(" de julio")
elif month == 8:
    print(" de agosto")
elif month == 9:
    print(" de septiembre")
elif month == 10:
    print(" de octubre")
elif month == 11:
    print(" de noviembre")
else:
    print(" de diciembre")
#-----------------------------------------------------------------------------------------------------------------------#
# miltiway vs sequential conditions statement:
# Use a mult-way conditional statement
value = int(input('enter 0 to 5'))
if value == 0:
    print("zero")
elif value == 1:
    print("one")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print("four")
elif value == 5:
    print("five")
print("Done")
# Use sequential conditional statements
value = int(input('enter 0 to 5'))
if value == 0:
    print("zero")
if value == 1:
    print("one")
if value == 2:
    print("two")
if value == 3:
    print("three")
if value == 4:
    print("four")
if value == 5:
    print("five")
print("Done")