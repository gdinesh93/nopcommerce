from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class Login:
    textbox_email_id='Email'
    textbox_password_id="Password"
    button_login_xpath="//*[contains(text(),'Log in')]"
    link_logout_xpath="//*[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID,self.textbox_email_id).clear()
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()


