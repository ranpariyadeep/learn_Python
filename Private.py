class Account:
    def __init__(self, username, password):
        self.username = username
        self.__password = password


    def get_password(self):
            print(self.__password)   # Method to access private variable

ac1= Account("user1", "pass123")    

ac1.get_password() 