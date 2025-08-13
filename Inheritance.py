class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")   

# BMW class inherits from Car class      
class BMW(Car):
    def __init__(self, model):
        self.model = model

car1 = BMW("X5")
car1.start()  # Output: Car started
car1.stop()   # Output: Car stopped
print(car1.model)  # Output: X5

#single inheritance example
class X5(BMW):
    def __init__(self, color, year):
        self.year = year
        self.color = color
        
car2 = X5("Black", 2020)
car2.start()

#multiple inheritance example
class i5(Car, BMW):
    def __init__(self, model, year):
        self.model = model
        self.year = year

        