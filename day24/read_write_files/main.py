# To open a file we use the open() function which takes two parameters, a file name and a mode. We store the result of this function in a variable. To read the content from the variable we use the read() function and store the result on another variable. After a file is opened we must close it to free resources
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Another way to open a file and not to forget to close it afterwards is to use the 'with' keyword and indent the operations we want to perform on that file inside a block of code. This way we don't have to use the close() instruction either
with open("my_file.txt") as f:
    contents = f.read()
    print(contents)

# To write on a file we must especify the mode atribute to "w" (write). This overwrites any content on the file. If the file doesn't exists yet it creates it
with open("my_file.txt", mode="w") as f:
    contents = f.write("New text.")

# If we want to add info to a file instead of overwrite it we must especify the mode atribute to "a" append. This mode also creates a file if it doesn't exists
with open("my_file.txt", mode="a") as f:
    contents = f.write("\nNew text.")

# There are other modes too:
# - fopen() is the key function to handle files
# - open() function takes two parameters; filename, and mode.
# - Modes for files opening:
#     - "r" - Read - Default value. Opens a file for reading, error if the file does not exist    
#     - "a" - Append - Opens a file for appending, creates the file if it does not exist    
#     - "w" - Write - Opens a file for writing, creates the file if it does not exist    
#     - "x" - Create - Creates the specified file, returns an error if the file exists


# Use absolute path
with open("C:/Users/felip/Desktop/tareas_entrevista.txt") as remote_file:
    contents = remote_file.read()
    print(contents)

# Use relative path
with open("../../../tareas_entrevista.txt") as remote_file2:
    contents = remote_file2.read()
    print(contents)
