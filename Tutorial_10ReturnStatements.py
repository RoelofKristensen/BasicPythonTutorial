# Return key word allows a function to return information, you cant put code after return statement
def cube(num):
    num*num*num
print(cube(3)) #this wil return nothing because all the function is suppose to do is cube a number

def cubertn(num):
    return num*num*num #the return statement wil replace cubertn with the answer
print(cubertn(4))
#storing the value that cube(num) brings
result = cubertn(5)
print(result)