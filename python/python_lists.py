InfoDb = []


# InfoDB is a data structure with expected Keys and Values

# Append to List a Dictionary of key/values related to a person and cars
InfoDb.append({
    "FirstName": "John",
    "LastName": "Mortensen",
    "DOB": "October 21",
    "Residence": "San Diego",
    "Email": "jmortensen@powayusd.com",
    "Owns_Cars": ["2015-Fusion", "2011-Ranger", "2003-Excursion", "1997-F350", "1969-Cadillac"]
})


# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Sunny",
    "LastName": "Naidu",
    "DOB": "August 2",
    "Residence": "Temecula",
    "Email": "snaidu@powayusd.com",
    "Owns_Cars": ["4Runner"]
})


#print(InfoDb[0])

# create dict
third = {
    "FirstName": "Nanu",
    "LastName": "Shadow",
    "DOB": "August 5",
    "Residence": "San Diego",
    "Email": "san@powayusd.com",
    "Owns_Cars": ["Jeep","4Runner"]
}

# add the dict to List
InfoDb.append(third)


# create dict
fourth = {
    "FirstName": "Lional",
    "LastName": "Messi",
    "DOB": "January 30",
    "Residence": "Barcelona",
    "Email": "LMessi@gmail.com",
    "Owns_Cars": ["Lamborghini","Maserati","Corvette"]
}

# add the dict to List
InfoDb.append(fourth)

InfoDb.append({
    "FirstName": "Dan",
    "LastName": "Mark",
    "DOB": "October 10",
    "Residence": "San Francisco",
    "Email": "DMark@yahoo.com",
    "Owns_Cars": ["2006 toyota sienna", "2011-Hellcat", "2003-Toyota Carolla"]
})


#print(InfoDb[len(InfoDb)-1])

# print function: given a dictionary of InfoDb content
def print_data(d_rec):
    print(d_rec["FirstName"], d_rec["LastName"])  # using comma puts space between values
    print("\t", "Residence:", d_rec["Residence"]) # \t is a tab indent
    print("\t", "Birth Day:", d_rec["DOB"])
    print("\t", "Cars: ", end="")  # end="" make sure no return occurs
    print(", ".join(d_rec["Owns_Cars"]))  # join allows printing a string list with separator
    print()
    
# for loop algorithm iterates on length of InfoDb
def for_loop():
    print("For loop output\n")
    for record in InfoDb:
        print_data(record)

for_loop()

# while loop algorithm contains an initial n and an index incrementing statement (n += 1)
def while_loop():
    print("While loop output\n")
    i = 0
    while i < len(InfoDb):
        record = InfoDb[i]
        print_data(record)
        i += 1
    return

while_loop()

#for loop with an index

print("for loop with index output\n")
# display indices in the list
for i in range(len(InfoDb)):
    print_data(InfoDb[i])
    
    
#for loop in a reverse order
for i in reversed(range(len(InfoDb))) :
    print_data(InfoDb[i])
    
#other methods that can be performed on the list
print("other methods that can be performed on lists: reverse()")
InfoDb.reverse()
while_loop()

# create new or add to dictionary data set with input
def addNewToInfoDb():
    #print("Enter a key:")
    key = input("Enter a key:")
    #print("Enter value:")
    value = input("Enter value:")
    InfoDb.append({key: value})
    print("You added " + key + " : " + str(value))

addNewToInfoDb()
