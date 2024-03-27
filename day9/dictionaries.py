# dictionary definition. We indent the keys inside the {} and we separate the keys using ,
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# retrieve a value from a dictionary
print(programming_dictionary["Bug"])

# add data to a dictionary by pasing a key name and assigning it a value. If the key we pass already existed in the dictionary then we will be editing it's value
programming_dictionary["Loop"] = "The action of doing something over and over again."

# create an empty dictionary or in case it already had content, this way you wipe the dictionary
dictionary = {}

# loop trough a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
