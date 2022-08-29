lucky_number = [4, 8, 15, 16 ,23 ,42]
friends =  ["Dulan", "Naunde", "jj", "Chane", "Dewald"]
#adding two lists together with extend
#friends.extend(lucky_number)

#adding values in list
friends.append("Eric")
#in what posision
friends.insert(4, "Ruben")
#removing a vaulue
friends.remove("Chane")
#resetting list
#friends.clear(friends)
#pop removes last element
print(friends.pop())
#finding specific value
print(friends.index("dewald"))
#sorting list Assending
friends.sort()
lucky_number.sort()
#Sorting list Desending
lucky_number.reverse()
print(friends)
print(lucky_number)
#you can copy a list
friends2 = friends.copy()
print(friends2)

#if list has double values. count them
people = ["hannes", "Jaco", "Jaco", "Pietie"]
print(people.count("Jaco"))
