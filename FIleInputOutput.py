#text Files : .txt, .docx, .log, .csv, .tsv
#binary Files : .jpg, .png, .gif, .mp4, .mp3, .zip

#python code to read and write files

# f = open('example.txt', 'w')  # Open a file in write mode
#         ("file_name", "mode") modes: read, write, append
#if mode not specified, it defaults to read mode

f = open('demo.txt', 'r')  # Open a file in write mode

line1 = f.readline()  # Read the first line of the file

print(line1)  # Print the first line

data  = f.read(5)  # Read the file content
print(data)  # Print the content of the file
f.close()  # Close the file


# meaning of Modes:
# 'r' - Read (default mode, file must exist)
# 'w' - Write (creates a new file or truncates an existing file)
   # truncates - it removes all content from the file before writing new content
# 'x' - Create a new File & Open it for writing(fails if the file already exists)
# 'a' - open for writing  (adds content to the end of the file)
# 'b' - Binary mode (used for binary files like images, videos)
# 't' - Text mode (default mode, used for text files)
#'+' - Read and Write (opens the file for both reading and writing)

# Example of writing to a file
f = open('demo.txt', 'w')  # Open a file in write mode
f.write("Add new .......\n")  # Write a line to the file
f.write("Demo\n")  # Write another line to the file
f.close()  # Close the file

f = open('demo.txt', 'a') 
f.write("I --- IGNORE ---\n")  # Append a line to the file
f.close()  # Close the file

#if file does not exist, it will create a new file
f= open('Sample.txt', 'a')  # Open the file in read mode


with open('Sample.txt', 'a') as f:  # Open the file in append mode
    f.write("This is a new line.\n")
    