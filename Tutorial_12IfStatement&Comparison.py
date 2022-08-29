'''#create a function taht determins the max number
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #other comparison operators <, >, =, <=, >=, !=
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else :
        return num3
print(max_num(4, 5, 3))
'''

name = print(input("Enter name: "))
passw = print(input("Enter password: "))

if name == "Rochelle":
    if passw == "Roelof":
        print("Passed")
    else:
        print("incorrect password")
else:
    print("incorrect name or password")

