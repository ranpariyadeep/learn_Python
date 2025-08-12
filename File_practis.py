with open("practis.txt", "w") as f:
    f.write("Hi Everyone\nwe are learning Java.\n")
    f.write("using Java\nI like to program in Java.\n")


with open("practis.txt", "r") as f:
 data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)  # Print the content of the file

with open("practis.txt", "w") as f:
    f.write(new_data)  # Write the modified content back to the file

with open("practis.txt", "r") as f:
    content = f.read()
    if(content.find("Python") != -1):
        print("Python is present in the file.")
    else:
        print("Python is not present in the file.")