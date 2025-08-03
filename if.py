if(5>3 and 5<10):
    print("5 is greater than 3")
    print("Checking if 5 is greater than 3")
elif(5<3 or 5==3):
    print("5 is less than 3")
else:
    print("5 is equal to 3")



# Single line if statement
food = "Pizza" 
#<variable> = <value> if <condition> else <value>
eat = "Yes" if food == "Pizza" else "No"
print(f"Do you want to eat {food}? {eat}")

#<sttement> if <condition> else <statement>
print("You can eat pizza") if food == "Pizza" or food == "Meggie"  else print("You cannot eat")

#Clever way to use if statement
#<variable> = (False_value, True_value)[condition]
age = 20
can_vote = ("You cannot vote", "You can vote")[age >= 18]
print(can_vote)