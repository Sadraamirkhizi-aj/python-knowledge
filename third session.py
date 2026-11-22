# concatenation ---> we can + int with int and float with float but when we want + str with str
                    # it gives "2" + "2" = 22 \ str + int = type error
print( 2 + 2 )
print ( 2.2 + 2.5 )
# operators over loading ---> use another advantage of (+) for str with str
print( "2" + "3" )
name = input("enter your name: ")
last_name = input("enter your last name:")
age = input("enter your age:")
 # there is three way to give a space ( " " ) (,) and (f" ") give a automatic space
print( "I am",name +" "+ last_name + " and i am  " + age + " year's old" )
print("i'm"+ name +" "+ last_name +" "+ age + " year's old" )
print(f"I'm {name} {last_name}, and i'm {age} years old ")

# escape sequence
print("  \"asdfghjk\"said sadra   ")
# print("C:\Users\Asus\PycharmProjects") # users part has error it fixed with two //
# print("C:\\Users\Asus\PycharmProjects")
print(r"C:\Users\Asus\PycharmProjects")

                                                #1 order its in order
#1-list collection data types ---> there are three type2 change its changeable          its with []
    # -4   -3     -2        -1                    #3 duplicate it can be duplicate
X = [ 1 , 5.3 , " sadra " , True]
    # 0   1      2          3
print(X)
# index
print(X[-3])
print(X[0])
