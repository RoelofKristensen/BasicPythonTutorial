#creating a dictionary, you can also have numbers as keys and assign them to a function
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Sep"])
print(monthConversions.get("Dec"))
print(monthConversions.get(input("enter month here: "), "Not a valid key")) #get function can also give you a default value if key is not found