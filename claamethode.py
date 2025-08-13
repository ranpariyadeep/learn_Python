class Person:
    name ="anonymous"  # class variable
    age = 0  # class variable
    
    # constructor
    def __init__(self, name, age):
        self.__class__.name = name
        self.age = age

    @classmethod
    def get_name(cls,name):
        cls.name = name
        print(cls.name)    

p1 =   Person("Alice", 30)
print(p1.name)  # Output: Alice
print(p1.age)   # Output: 30
print(p1)  # Output: <__main__.Person object at 0x...>
print(Person.name)  # Output: Alice
p1.get_name("Rahul")  # Output: 
print(p1.name) 