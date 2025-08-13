
#del keyword is used to delete object properties or objects self

class Student:
    def __init__(self, name):
        self.name = name

S1 = Student("Alice")

del S1 # Deleting the object S1
print(S1)  # This will raise an error because S1 has been deleted