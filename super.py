class Car:

    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")   

# BMW class inherits from Car class      
class BMW(Car):

    def __init__(self, model,type):
        super().__init__(type)   # Call the parent class constructor
        self.model = model

car1 = BMW("X5", "SUV")
car1.start()  # Output: Car started
car1.stop()   # Output: Car stopped
print(car1.model)  # Output: X5
print(car1.type)   # Output: SUV