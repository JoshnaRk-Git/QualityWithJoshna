from selenium.webdriver.common.by import By
from Test.TestData import UserNameLoc, PasswordLoc, LoginButtonLoc,errorMessageLoc
class loginPage:

    def __init__(self,driver):
        self.driver=driver

    def open(self,url):
        self.driver.get(url)

    def enterUsername(self, username):
        self.driver.find_element(*UserNameLoc).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*PasswordLoc).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*LoginButtonLoc).click()


    def getError(self):
         try:
             return self.driver.find_element(*errorMessageLoc)
         except:
             return


