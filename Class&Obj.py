#creating a class
class Student:
    college_name = "ABC University"  # class variable
    #constructor 
    def __init__(self,fullname):
       self.name = fullname
       print("adding a new student")



#creating an object
student1 = Student("Alice")
print(student1.name)  # Output: Alice


#####################################################

class Car:
    motor = False
    #constructor - default constructor
    def __init__(self):
        pass

    #perameterized constructor
    def __init__(self,brand, color): 
        self.brand = brand
        self.color = color   

    #method
    def engine_start(self):
        if(self.motor == False):
         print("Engine started")
         self.motor == True
    def engine_stop(self):
        if(self.motor == True ):
         print("Engine stopped")
         self.motor == False    

    @staticmethod #decorator
    def car_info():
        print("This is a car class.")     
    

c1 = Car("BMW", "Blue")


print(c1.brand)  # Output: Toyota
print(c1.color)  # Output: Red    
c1.engine_start()  # Output: Engine started
c1.car_info()  # Output: This is a car class.

#####################################################

