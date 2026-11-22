# input data
# name = input("what is your name?")
# print("hello " + name)

# #converter
# str_string = "salam"
# str_string = bool(str_string)
# print(type(str_string))
# num_string = "33"
# num_string = bool(num_string)
# print(type(num_string))
# sym_string = "!"
# sym_string = bool(sym_string)
# print(type(sym_string))
# bool_string = "False"
# bool_string = str(bool_string)
# print(type(bool_string))

# name = input( "enter your name: ")
# last_name = input( "enter your last name: ")
# age = input( "enter your age: ")
# print( "i am " + name + " " + last_name + " and im " + age + " years old" )
# print(f"i am {name} {last_name} and i am {age} years old")
                                   #    1-list:ordered-changeable-duplicated
                                   #    2-tuple:ordered-unchangeable-duplicated
# # there are four type of collection ---> 3-dictionary:unordered-changeable-duplicate(value)
                                   #    4-set:changeable-unordered-no duplicate
#  #1
# A = [1,2.2,2.2,"this is list",True]
# print(A)
# print(A[3])
# print(A[-1])
#
# # 2
# S = ("baba","maman",2.2,False,"this is tuple")
# print(S)
# print(S[-1])
# print(S[3])
#
# # 3
# D = {"a":1.1,"b":2.2,"c":3.3}
# print(D)
# print(D["a"])
#
# # 3
# F = {1,3,5,9,74,5,3,69}
# G = {1,3,4,69,8,6,3,85}
#  # set has som mathematical options
#
# # u union
# print(G.union(F))
# print(F.union(G))
# # output :{1, 3, 4, 69, 6, 5, 8, 9, 74, 85} {1, 3, 4, 69, 5, 6, 8, 9, 74, 85}
#
# # intersection == subscription of two list (inter somthing)
# print(G.intersection(F))
# print(F.intersection(G))
# # output : {1, 3, 69} {1, 3, 69}
#
# # difference == first set minus second set (difference = تفاوت)
#
# print(G.difference(F)) # take every equal num in () from ().
# print(F.difference(G))
# # output :{8, 4, 85, 6} {9, 74, 5}
#
# # symmetric difference == sum two set
#
# print(G.symmetric_difference(F))
# print(F.symmetric_difference(G))
# # output : {4, 5, 6, 8, 9, 74, 85} {4, 5, 6, 8, 9, 74, 85}
#
# # list method
#
# my_games = ["god of war","devil may cry","assassins creed`s","the crew 2"]
# print(my_games)
#
# print(my_games.index("god of war")) # say the index number 0,1,2
# print(my_games.count("the crew 2"))
# print(my_games)
# # manipulate
#
# # add
# my_games.append("far cry")
# my_games.insert(3,"spider-man")
# print(my_games)
#
# # remove
# my_games.remove("the crew 2")
# print(my_games)
# my_games.pop(2)
# print(my_games)
#
# deleted = my_games.pop(2)
# print(deleted)
# print(my_games)
# print(len(my_games)) # count
#
# games = my_games.copy() # copy list to another list
# print(games)
#
# games.reverse()
# print(games)
#
# games.sort() # sort by alphabet
# print(games)
# games.sort(reverse=True) # sort by alphabet then reverse it
# print(games)
# games.sort(reverse=False)
# print(games)
#
# games.clear()  # delete every thing in list
# print(games)

# test_dicts = {"a":200,"b":300,"c":400,"d":500,"e":600}
# print(test_dicts)
# print(test_dicts.keys())
# print(test_dicts.values())
#
# print(test_dicts.get("a"))
# # tax amount
# print("tax system code running")
# tax = int(input("enter salary amount: "))
#
# if tax < 10000000:
#     tax_amount = 0
#     print("you do not have tax:", tax_amount)
#
# elif 10000000 <= tax <= 20000000:
#     tax_amount = tax * 0.1
#     print("your tax is:", tax_amount)
#
# elif tax > 20000000:
#     tax_amount = tax * 0.2
#     print("your tax is:", tax_amount)
#
# # grading system
# print("lets find your grade")
# grade = int(input("enter your grade: "))
# if 90<= grade <= 100:
#     print("your grade result is:A")
# elif 80 <= grade <= 89:
#     print("your grade result is:B")
# elif 70 <= grade <= 79:
#     print("your grade result is:C")
# else:
#     print("your grade result is:Fail")
#
# # type of number
# number = int(input("enter your number: "))
# if number == 0:
#     print("your number is:0")
# elif number > 0:
#     print("your number type is positive")
# else:
#     print("your number type is negative")
#
# # gym membership system
# print("hello to sadra gym")
# age = int(input("enter your age: "))
# if age < 18 :
#     print("your payment price is :700 rial")
# elif 18 <= age < 60 :
#     print("your payment price is :1000 rial")
# elif 60 <= age < 80:
#     print("your payment price is :2000 rial")

# currency_1 = int(input("What do you have left in pesos?" ))
# currency_2 = int(input("What do you have left in soles?" ))
# currency_3 = int(input("What do you have left in reais?" ))
# totall = (currency_1 + currency_2 + currency_3)*0.21
# print(totall)


# list
first_list = ["zahra",33,True,33.5]
print(first_list)
print(first_list[1])
print(first_list[-3])


my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list)

print(my_list[0:3])
print(my_list[0:3:1])
print(my_list[-4:-2])
print(my_list[1:])
print(my_list[::-1])
print(my_list[-2:-5:-1])
print(my_list[0:5:2])


first_tuple = {0,3,5,4,8}

first_dict = {"sadra":33,"zahara":88}

first_set = {2,525,4,3,5}
second_list = [2,83,85,33]