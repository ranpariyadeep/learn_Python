import random
import string

# random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#                'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                'i', 'j', 'k', 'l', 'm', 'n', 'o',
#                'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z',
#                '@', '#', '$', '%'] )

password_length = 16
password = ""
char = string.ascii_letters + string.digits + string.punctuation
random.choice(char)

for i in range(password_length):
    password += random.choice(char)

print("Your random password is: ", password)

#list comprehension -other method
#[function for i in range()] give ans in list

#.join used for join all string or char of list 
# ex. [a,gg,v] conver into "aggv"
res = "".join([random.choice(char) for i in range(password_length)])
print(res)