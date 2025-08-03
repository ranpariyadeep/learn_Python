

# variables.py
# Rules for variable names:
# 1. Variable names can contain letters, numbers, and underscores.
# 2. They cannot start with a number.

name = "Deep Ranpariya" #string
p = 'A'  #character (not a standard type in Python, but can be treated as a string of length 1)
age=24        #integer
price = 100.50 #float

print(f"Hello, my name is {name} and I am {age} years old.")  
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(price)) # Output: <class 'float'>
print(type(p))    # Output: <class 'str'> (single character is still a string in Python)
print()

age=25
age2 = age
print(f"Hello, my name is {name} and I am {age2} years old.") 

#Data types
# 1. String 
# 2. Integer  +ve, -ve, 0
# 3. Float
# 4. Boolean
# 5. None

Is_active = True #boolean
Is_deleted = False #boolean
print(f"Is the user active? {Is_deleted}")     

print(f"Is the user active? {Is_active}")

n = None #NoneType
print(f"The value of a is: {n}")

a= 11
b= 12
print(a+b) # output : 23
#f variable ne print karva maate use thay che 
print(f"{a}+{b}") # output : 11+12
print(f"{a}+{b}={a+b}") # output : 11+12=23
