#creating own function
def say_hi():
    print("Hello User")

#If you want to Run your function then you will "call" it
say_hi()

#adding parameteres. allowing yourself to edit a function
def hello(name): #name is a varaible that can be used within the function
    print("Hello " + name)
hello("Roelof") #variable name is replaced with Roelof
hello("Rochelle")

#you can also add more parameters
def more(name, age):
    print("Hello " + name + ". You are " + str(age))
more("Rochelle", 18)