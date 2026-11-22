# tuple methods
phone_number = ("09026291433","09142396627","09144038504")
# we write phone numbers in string because int cannot start with 0

print(phone_number.index("09026291433"))
print(phone_number.count("09142396627"))

# dict method
products = {"apple":2000,"orange":2001,"banana":2002,"cherry":2000}
print(products)

# info
print(products.items())
# output dict_items([('apple', 2000), ('orange', 2001), ('banana', 2002), ('cherry', 2000)])
print(products.keys())
print(products.values())

print(products.get("apple"))
print(products.get("tangerine"))
# print(products["tangerine"]) error

# manipulate
products.pop("cherry")
print(products)

products.popitem()
print(products)

products2 = products.copy()
print(products2)

products2.clear()
print(products2)

fruits = {"sib" : 20008,"pineapple":2006}
products.update(fruits)
print(products)

color_list = ["red","blue","green"]
color = dict.fromkeys(color_list,33)
print(color)

products.setdefault("sib",2025)
print(products)

products.setdefault("ananas",2000)
print(products)

# set
games = {"red dead redemption","god of war ","sekiro"}
games_2 = {"spiderman","nfs"}
print(games)

# info
print(games.issubset(games_2))
print(games_2.issubset(games))
print(games.isdisjoint(games_2))
print(games_2.issuperset(games))
print(games.issuperset(games_2))
# manipulate
games.pop() #random
print(games)

games.update(games_2)
print(games)

games.remove("nfs")
print(games)

games.discard("nfs")
print(games)
games.add("nfs")
print(games)

print(games_2)
print(games)

games.intersection_update(games_2)
print(games)

games.symmetric_difference_update(games_2)
print(games)

games.difference_update(games_2)
print(games)

# name|last_name input ---> {key(name+last_name):value([student])}

# f_name1 = input("enter your first name: ")
# l_name1 = input("enter your last name: ")
#
# f_name2 = input("enter your first name: ")
# l_name2 = input("enter your last name: ")
#
# f_name3 = input("enter your first name: ")
# l_name3 = input("enter your last name: ")
#
# full_name1 = f"{f_name1} {l_name1}"
# fullname2 = f"{f_name2} {l_name2}"
# fullname3 = f"{f_name3} {l_name3}"
#
# student = [full_name1,fullname2,fullname3]
# student_dict = dict.fromkeys(student, "student")
# print(student_dict)

work_dict = {"A":1,"B":2,"C":3}
X1 = input("enter: ")
X2 = input("enter: ")
X3 = input("enter: ")

work_dict["A"] = X1
work_dict["B"] = X2
work_dict["C"] = X3
print(work_dict)

cl_dict = {"b":1,"c":2,"d":3}
cl_dict = list(cl_dict.items())
user_index = int(input("enter index : "))
print(cl_dict.pop(user_index))



