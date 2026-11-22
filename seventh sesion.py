# loop ; we have two types of loop ---> we know when it gonna ends and not know
# we have two types of loop for and while
# we can write for just in tuple str list
# if we want to repeat this loop we use for i range(x, y)
a = [1, 2, 3, 4]
for i in a:
    if 7 in a:
        print(i)
    else:
        for i in range(0, 5):
            print(i)

names = []
for i in range(3):
    names.append(input("enter your name: "))
    if names not in names:
        print("invalid name")
    else:
        names.append(input("enter your name: "))
        print(names)

names = []
names_test = []
for i in range(5):
    name = input("enter your names: ")
    if name in names:
       names_test.append(name)
       counter = names_test.count(name)
       name = f"{name} {counter+1}"
       names.append(name)
    else:
       names.append(name)
print(names)
a = [1,2,3,4,5]
print(a[0:3:2])


