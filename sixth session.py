# if statement
x = [2,3,4,5,6,True]
if True in x: # in is a membership statement
    print("has")
elif 2 in x:
    print("bye")
else:
    print(None)

num = int(input("enter num: "))
A = [1,2,3,4,5]
if num in A:
    print(f"{num} is in {A}")
else: print(f"{num} is not in {A}")

# = assignment operator | ==,> <, <= >=, !=(na mosavi) comparison operator | arithmetic operators

age = int(input("enter age: "))
if 1 <= age < 100:
    print(f"{age} is registered")
else :
    print(f"{age} is not registered")

name_1 = input("enter name: ")
name_2 = input("enter name: ")
name_3 = input("enter name: ")

if  name_1 or name_2 != name_3 != name_1:

        print([name_1, name_2, name_3])
else :
        print( "names are duplicate" )

# calculator
print("calculator running ")
num = int(input("enter num: "))
num2 = int(input("enter num2: "))
print("enter operation type: \n1.+\n2.-\n3.*\n4./\n5.**\n6.//\n7.%")
operation = int(input("enter operation: "))
if operation ==1:
    print(num + num2)
elif operation == 2:
    print(num - num2)
elif operation == 3:
    print(num * num2)
elif operation == 4:
    print(num / num2)
elif operation == 5:
    print(num ** num2)
elif operation == 6:
    print(num // num2)
elif operation == 7:
    print(num % num2)
else:
    print("invalid operation")

# imports
# import math
# num = int(input("enter num: "))
# print(math.log(num))
# print(math.ceil(num))
# print(math.floor(num))
# print(math.cos(num))
















