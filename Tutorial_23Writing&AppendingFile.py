


employee_file = open("Tutorial_22ReadingFiles.text", "a") #Appending to files
#employee_file.write("Tom - Human Resourcess") #be carefull you can mess up file

employee_file.write("\nKelly - Customer Service")

#employee_file = open("Tutorial_22ReadingFiles.text", "w") #overwrite files with only new elements
#employee_file.write("\nKelly - Customer Service")  kelly would be the only one in the file
employee_file.close()

#you can also create a new file with "w"
employee_file = open("Tutorial_22ReadingFiles1.text", "w")
employee_file.close()