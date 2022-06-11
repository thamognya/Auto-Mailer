import login

from random import randrange
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class main_class:
    def __init__(self):
        pass
    def main(self):
        login_class = login.login_class()
        useragent_used = login_class.useragent()

        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", useragent_used)

        driver = webdriver.Firefox(profile)
        driver.get("http://www.whatsmyua.info/")

        print(login_class.email())
        print(useragent_used)
        

if __name__ == "__main__":
    main = main_class()
    main.main()
