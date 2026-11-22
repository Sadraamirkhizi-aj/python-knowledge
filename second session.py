# data types

# string---> mean just its characters
print("aB12#")
# integer---> just z numbers
print(123)
# float---> just decimal numbers
print(2.45)
# boolean---> true and false
print(True)
print(False)
print(2*5==10)
print(2*8==64)
# PEPE8---> it's the rule for same style coding
# arithmetic operators---> guide for operators
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 ** 3)
print(2 // 2)
print(2 / 2)
print(7 % 2)
#(=)=assignment operators

# type---> the data type detectors
print(type("sadra"))
print(type(2654))
print(type(2.2))
print(type(True))
print(type(False))

                     #1.alphabet,num, (_)
# variable rules--->  2.cant start with num  no pythonic words
                     #3.case sensitive

# unwritaable rule---> the variable must be brief and useful
x= 2*2
print(x)
X = 5-2
print(X)
your_name = "sadra"
print(your_name)

# variable overwriting
email_username = "sadra12.com"
email_username = "sadra123.com"
print(email_username)

# input--->enter data
name = input("Enter your name: ")

lastname = input("enter your last name: ")

age = input("enter your age: ")
print(name)
print(lastname)
print(age)

# after the user enter the amount of a
a = input("enter your number: ")
print("the result is: ",a)
# now we want to do some math work on a
a = input ("enter a number: ")
print("the result is: ",float(a)*10-6*2)

#some uses of input
h = input( "height is: " )
w = input( "the width is: " )
print("the area is: ",int(h) * int(w))
print("the perimeter is: ",(int(h) + int(w)) * 2)

# type casting---> convert types
num_string = "5"
num_srting = int(num_string)
print(type(num_srting))
num_srting = ""
num_srting = str(num_srting)
print(type(num_srting))
# sym_string never can be num(sym_string)
# every data type can be string (str)
# bool just can be str
# num can be every data type except sym_string

#there is another way
a=20
b=4
x=a/b
print(x)
# the run answer is 5.0 (float)
# now we wnt to convert it to int
print(int(x))