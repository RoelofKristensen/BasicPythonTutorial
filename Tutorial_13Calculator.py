
num1 = float(input("Enter first number: "))
opp = input("enter opperator: ")
num2 = float(input("Enter second number: "))
if opp == "+":
    print(num1 + num2)
elif opp == "-":
    print(num1 - num2)
elif opp == "*":
    print(num1 * num2)
elif opp == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

