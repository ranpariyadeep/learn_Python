#tuples is a collection of ordered elements that are immutable.
#Tuples are immutable, meaning they cannot be changed after creation.
tup1=() # Empty tuple
tup2=(1,)  # Single element tuple, note the comma
tup3=(1, 2, 3)  # Multiple elements tuple


tup = (22, 45, 67, 89, 90)
print(tup)  # Output: (22, 45, 67, 89, 90)
print(tup[0])
print(tup[1:3])  # Output: (45, 67)
print(tup[-1])  # Output: 90
print(tup[-3:])  # Output: (67, 89, 90)
print(tup[:2])  # Output: (22, 45)

print(len(tup))  # Output: 5    

tup.count(22)  # Output: 1, how many times 22 in tuple
tup.index(67)  # Output: 2, index of first occurrence of 67
 