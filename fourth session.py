# learn some new collection
# 2-tuple ---> same as list has duplicated and ordered and created with ()
sadra = ("baba","tara","maman","sadra","baba")

print(sadra)
print(sadra[2])
print(sadra[-1])

# 3-dictionary ---> uses with {} and "a" = key | print with[]
# 4 = value. key cannot be duplicate,changeable but value can both
A = {"Argentine":"Messi","Brazil":"Neymar","France":"Zeidan","England":"Kane","Y":True}
print(A)
print(A["England"])
print(A["Argentine"])
print(A["Brazil"])
print(A["France"])
print(A["Y"])

# 4-set ---> uses with {} and like majmue, unordered ,no duplicate, changeable
C = {1,2,5,6}
D = {3,2,4,6}
print(C.union(D)) # u
print(D.union(C))

print(D.intersection(C)) # eshterak
print(C.intersection(D))

print(C.difference(D)) # - take every equal num in () from ().
print(D.difference(C))

print(C.symmetric_difference(D)) # tafazol motagaren
print(D.symmetric_difference(C))

# 1-list methods * none of the list method don`t need []
cars = ["prado","cla 250","s500","patrol","camaro"]
print(cars)

#info
print(cars.index("cla 250"))
print(cars.count("prado"))

# manipulate
cars.append("911") # ---> add
print(cars)

cars.insert(3,"dodge") # ---> add with info
print(cars)

cars.remove("s500") # --->remove
print(cars)

cars.pop(0)
print(cars)

dropped = cars.pop(1)
print(dropped)
print(cars)
print(len(cars))

cars2= cars.copy()
print(cars2)

cars2.reverse()
print(cars2)

cars2.sort() # sort by alphabet
print(cars2)

cars2.sort(reverse=True) #sort by alphabet then reverse it
print(cars2)

cars2.clear()
print(cars2)

iranian_cars = ["207","pride","206","dena"]
cars.extend(iranian_cars)
print(cars)

X = [1,2,3,4,5]
Y = [6,7,8,9,10]
X.append(Y)
print(X)
print(X[5][2])
import this