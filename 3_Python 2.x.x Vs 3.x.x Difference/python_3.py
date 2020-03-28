#1. print function

print("karthi")

# 2. Python 3 stores data unicode as default

#unicode
a = "karthi"
print(a, type(a))
#bytes
b = b"karthi"
print(b, type(b))

#3 input from user

name = input("Please enter your name: ")
print("hi {}".format(name))

#4 input from user

calc = eval(input("Enter '6 / 3' I will do action on user input.. so caution while using me... : "))
print("My output ", calc)

#5 range function
print(range(10))


#6 int number division
print("5/4 in python-3 is ",5/4)
print("5//4 in python-3 is ",5//4)

#7 Exception handling also...

try:
    trying_this
except NameError as error:
    print(error, "we got error") 

# this also

num = 10
if num == 10:
    raise IOError("file error")
