from selenium.webdriver.common.by import By
#Locators
UserNameLoc =(By.CSS_SELECTOR,"#user-name")
PasswordLoc =(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
LoginButtonLoc=(By.ID,"login-button")
errorMessageLoc=(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")


#Login Testdata
ValidUsername= "standard_user"
ValidPassword = "secret_sauce"
URL= "https://www.saucedemo.com/"
InvalidUsername="std_user"