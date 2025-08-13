#Hiding the implementation details of a Car class
#and exposing only the necessary methods

class Car:

    def __init__(self):
       
        self.acc = False  
        self.speed = 0
        self.brk = False
        self.clutch = False

    def start(self):
          self.clutch = True
          self.acc = True
          print("Car started")

Car1 = Car()
Car1.start()  # Output: Car started          