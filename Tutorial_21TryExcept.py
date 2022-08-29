#if you want your program to try code and give default answer if input is invalid to protect our program

try:
    number = int(input("Enter number: "))
    print(number)
except:  # will  accepts all errors. so isn't specific
    print("Invalid Input")

try:
    value = 10/0
    number = int(input("Enter number: "))
    print(number)
except ZeroDivisionError as err: #storing ZeroDivisionError in err variable
    print(err) #and then printing it
except ValueError:
    print("Invalid Input")