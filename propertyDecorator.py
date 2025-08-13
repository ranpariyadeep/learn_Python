class Student:
    college_name = "ABC University"
    # constructor
    def __init__(self, phy,math,chem):
        self.phy = phy
        self.math = math
        self.chem = chem

# property decorator used for  if we change the value of phy, math or chem then percentage will automatically change

#
    @property
    def percentage(self):
        return str((self.phy + self.math + self.chem) / 3) + "%"

student1 = Student(85, 90, 95)
print(student1.percentage)  # Output: 90.0%

student1.phy = 88
print(student1.percentage)  # Output: 91.0%