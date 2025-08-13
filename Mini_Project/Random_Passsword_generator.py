import random
import string

# create a randome password 
# also check in password min 3 digit exsit or not 
# any how many attempt they try to create a password 
# min. length is 9

# random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#                'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                'i', 'j', 'k', 'l', 'm', 'n', 'o',
#                'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z',
#                '@', '#', '$', '%'] )

password_length = 9
password = ""
num = ["0","1","2","3","4","5","6","7","8","9"]

char = string.ascii_letters + string.digits + string.punctuation


def gen_pass(attempt=1):
  res = [random.choice(char) for i in range(password_length)]
  count=0
  
  for i in res:
      if(i in num):
         count +=1
         if(count == 3):
          print("Your random password is: ", "".join(res))
          print(f"Total attempts: {attempt}")
          
          return
        
  gen_pass(attempt+1);   


gen_pass();  








#list comprehension -other method
#[function for i in range()] give ans in list

#.join used for join all string or char of list 
# ex. [a,gg,v] conver into "aggv"
# res = "".join([random.choice(char) for i in range(password_length)])
# print(res)