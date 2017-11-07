# In python to control stings there is a 4 tags to use to alter string
# let's start with \n (Next Line)
# following line will print the output of a and b in next line.
print("a\nb")
# another is known as \t (tab)
# following line will leave a tab space between a and b
print("a\tb")
# and the third is \b (back space)
# it will remove b from the list and print acd
print("ab\bcd")
# fourth in this line is \a ()alert or bell
# this will leave a space between the letters, for comparison i have print same abc in here one with \a and one without.
# i haven't find any usefull places for \a but if i will i will update files
print("a\a b\a c\a")
print("abc")
# and there is two more tags \' and \"
# This is usefull as you are using only ' in print statement and " in words or " in print and ' in words.
# here's one example
print("choose your 'words' carefully..")
print('choose your "words" carefully..')
print("choose your \"words\" carefully..")
print('choose your \'words\' carefully..')
# and to print \ use double \\
x='c:\\users\\account\\personal'
print(x)
#-----------------------------------------------------------------------------------------------------------------------#
# now lets use string formatting tools
# for example let's make a program in where we will print the power of 10 of few numbers.
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)
print(11, 10**11)
print(12, 10**12)
print(13, 10**13)
print(14, 10**14)
print(15, 10**15)
# let's try formet function to print numbers in format as we wan't.
print('{0:>3}{1:>16}'.format(0, 10**0))
print('{0:>3}{1:>16}'.format(1, 10**1))
print('{0:>3}{1:>16}'.format(2, 10**2))
print('{0:>3}{1:>16}'.format(3, 10**3))
print('{0:>3}{1:>16}'.format(4, 10**4))
print('{0:>3}{1:>16}'.format(5, 10**5))
print('{0:>3}{1:>16}'.format(6, 10**6))
print('{0:>3}{1:>16}'.format(7, 10**7))
print('{0:>3}{1:>16}'.format(8, 10**8))
print('{0:>3}{1:>16}'.format(9, 10**9))
print('{0:>3}{1:>16}'.format(10, 10**10))
print('{0:>3}{1:>16}'.format(11, 10**11))
print('{0:>3}{1:>16}'.format(12, 10**12))
print('{0:>3}{1:>16}'.format(13, 10**13))
print('{0:>3}{1:>16}'.format(14, 10**14))
print('{0:>3}{1:>16}'.format(15, 10**15))
# Now let's understand this formatting function, that how it works.
# In format function '{0:>3}{1:>16}' is a comment that what you really want to pritn in the function and at which point.
# And format.(2,10**2) is a function where we pass the values which we want to be in formatting.
# In '{0:>3}{1:>16}', {0:>3} defines the right sjustify the first three character.
# And in {1:>16} it defines the limit of second line 10**2, where it defines right justify whithcin 16 characters.
#-----------------------------------------------------------------------------------------------------------------------#
# Now it's time to see some multiline strings.
# To print multi line string you must use ' ' or " " to define the string with variable name.
x = 'Hi how are you?'
print(x)
print(type(x))
# to print multiple line string you need to use ''' ''' or """ """  3 quotes.
x = ''' Hi, I am okay,
     I hope you are doing okay,
      because of this storm in your area.'''
print(x)
print(type(x))
#-----------------------------------------------------------------------------------------------------------------------#
# now let's try some controling print fnction.
# end='' is a keyword argument, which is totally oposite of \n keyword.
# When we use \n it starts the next argument in next line and if we use end='' it will start with next space available,
# means it won't leave any space.
# lets try example.
print('enter:' ,end='')
print(end='enter')
print('hi')
# you will see that last three line will leave no space between characters, it will print as soon as there is a space.
# there is one more keyword known as sep='',
# this is useful when we have t seprate string with some string,
# let's don't get bored and see some examples for better understandings.
a,b,c,d= 10,20,30,40
print(a,b,c,d)
print(a,b,c,d, sep='')
print(a,b,c,d,sep='-')
print(a,b,c,d,sep=':')
print(a,b,c,d,sep=',')
# as we can see from output that thre will be no space when use sep='', we have to define some string to differenciate bvetween them.
