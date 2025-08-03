#String is immutable, meaning it cannot be changed after creation.
str1 = "This is a string"
str2 = 'This is another string'

str3 = """This is a multi-line string
that spans multiple lines."""

str4 = '''This is also a multi-line string
that can be defined using single quotes.'''

print(str1)
print(str2)
print(str3)
print(str4)


#Concatenation
str5 ="Deep"
str6 = "Ranpariya"
new_str = str5 + str6  # Output: DeepRanpariya
new_str_with_space = str5 + " " + str6  # Output: Deep Ranpariya
print(str5 + str6) # Output: DeepRanpariya
print(str5 + " " + str6)  # Output: Deep Ranpariya

#length of string
print(len(str1)) # Output: 16
length = len(str2)  # Output: 22
print(len(new_str)) # Output: 13
print(len(new_str_with_space)) # Output: 14

#Indexing
print(new_str_with_space[0])  # Output: D
 # indexing thi string ya Char ne change no kari sakay

 #Slicing
 #Starting index is inclusive, ending index is exclusive
 #last thi count karva maate -1 thi start kariye
 #new_str_with_space = "Deep Ranpariya"
print(new_str_with_space[0:4])  # Output: Deep
print(new_str_with_space[5:])  # Output: Ranpariya
print(new_str_with_space[:6])  # Output: Deep R
print(new_str_with_space[-1])  # Output: a (last character)
print(new_str_with_space[-3:])  # Output: iya (last three characters)
print(new_str_with_space[-4:-2]) # Output: iy (last four characters, excluding the last two)