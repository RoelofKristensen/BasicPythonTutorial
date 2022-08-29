#creating a boolean
is_male = False
is_tall = True

if is_male and is_tall:# can also use or,
    print("you are a tall male") #will execute if statement is true
elif is_male and not(is_tall):
    print("you are a short male")
elif is_tall and not(is_male):
    print("you are not a male but tall")
else:
    print("you are not a male and short")#will execute if statement is false