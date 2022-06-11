from random import randrange
from fake_useragent import UserAgent

# path of webdriver
class login_class:
    def __init__(self):
        pass
    def random_num(self):
        return randrange(10)
    def useragent(self):
        useragent = UserAgent()
        return useragent.random
    def email(self):
        if (self.random_num() == 0):
            email = "something"
        elif (self.random_num() == 1):
            email = "something"
        elif (self.random_num() == 2):
            email = "something"
        elif (self.random_num() == 3):
            email = "something"
        elif (self.random_num() == 4):
            email = "something"
        elif (self.random_num() == 5):
            email = "something"
        elif (self.random_num() == 6):
            email = "something"
        elif (self.random_num() == 7):
            email = "something"
        elif (self.random_num() == 8):
            email = "something"
        elif (self.random_num() == 9):
            email = "something"
        else:
            email = "something"

        return email

