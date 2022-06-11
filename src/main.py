# import files
import login
# import libraries
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# make a main class
class main_class:
    def __init__(self):
        pass
    def main(self):
        # make a login class
        login_class = login.login_class()
        # get a useragent
        useragent_used = login_class.useragent()
        # get profile
        profile = webdriver.FirefoxProfile()
        # use custome profile
        profile.set_preference("general.useragent.override", useragent_used)
        # use the profile
        driver = webdriver.Firefox(profile)
        # open this website to check if the useragent is working
        driver.get("http://www.whatsmyua.info/")
        # print the email
        print(login_class.email())
        # print user agent used
        print(useragent_used)
        

if __name__ == "__main__":
    # make a main class
    main = main_class()
    # run the main function
    main.main()
