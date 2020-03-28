#1. print function

print "karthi"

# 2. Python 2 stores data ascii as default

#ascii 
a = "karthi"
print a, type(a)
# unicode - utf-8
b = u"karthi"
print b, type(b)

#3 raw_input from user is equal to input in python 3 

name = raw_input("Please enter your name: ")
print("hi " + name)

#4 input from user similar to eval(input())

calc = input("Enter '6 / 3' I will do action on user input.. so caution while using me... : ")
print("My output ", calc)
#5 xrange and range function

print(range(10))
print(xrange(10))

#6 int number division
print("5/4 in python-2 is ",5/4)
print("5//4 in python-2 is ",5//4)

print("we have to use 5.0/4.0 -- ", 5.0/4.0)

#7 Exception handling also...

try:
    trying_this
except NameError, error:
    print error, "we got error"

# this also

num = 10
if num == 10:
    raise IOError, "file error"
