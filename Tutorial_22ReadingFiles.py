# can open files in different modes "r" = read, "w" = write, "a" = append (add to the end), "r+" = read and write
#Storing file inside variable
employee_file = open("Tutorial_22ReadingFiles.text", "r")

print(employee_file.readable()) #will check is file is readable and return True or False

#print(employee_file.readline())  will move like a cursour  first line
#print(employee_file.readline())  then print second line

#print(employee_file.readlines()[3]) or you can use this to read multiple lines or chosen lines
for employee in employee_file.readlines():
    print(employee)

employee_file.close()



#opening with contex manager is the best. you dont have to close
'''with open("Tutorial_22ReadingFiles.text", "r") as file:
    yow write here and if the indent is removed it wil automaticaly close the file'''