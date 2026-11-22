# creating pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# print(2,end = "-" )
# print(3,end = "\n")
# for i in range(1,5+1):
#     for j in range(i,0,-1):
#         print (j,end =' ' )
#     print()
# for i in range(5+1,1):
#     for j in range(j+1,-1):
#         print (j,end =' ' )
#     print ()
# k = 7
# for i in range (1,5+1):
#     for j in range (1, k-i ):
#         print(j, end=" ")
#     print()
# i = 5
# for i in range (5,0,-1):
#     for j in range (i,0,-1):
#          print(j, end=" ")
#     print()
# while loop
# names = []
# while len(names)<3:
#     name = input("Enter a name: ")
#     if name not in names:
#      names.append(name)
#     elif name in names:
#         print("Sorry, the name you entered is already in use.")
# print(names)
for i in range(1, 5+1):
    for j in range(6-i, 0, -1):
        print(j, end=' ' )
    print()

for i in range(1,5+1):
    for j in range(5,5-i, -1):
        print(j, end=' ')
    print()



