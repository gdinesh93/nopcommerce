import re
import string
import random
import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.AddCustomer import AddCustomer
from utilities.readproperties import Readconfig
from PageObjects.LoginPage import Login
from utilities.customlogger import Loggen

class Test_003_add_customer:
    baseurl=Readconfig.getapplicationurl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    logger=Loggen.log()

    def email_generator(self):
        p = ''
        for i in range(8):
            x = random.choice(string.ascii_lowercase + string.digits)
            p = p + x
        return p + "@gmail.com"

    def password_generator(self):
        p=""
        for i in range(8):
            x=random.choice(string.ascii_letters+string.digits)
            p=p+x
        return p

    def fnamegenerator(self):
        p=random.choice(["Ava", "Ethan", "Mia", "Liam", "Sophia",
        "Jackson", "Isabella", "Noah", "Charlotte", "William", "Harper"])
        return p

    def lnamegenerator(self):
        p=random.choice(["Smith", "Johnson", "Williams", "Jones",
        "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson"])
        return p
    def gendergenerator(self):
        p=random.choice(["Male",'Female'])
        return p

    @pytest.mark.sanity
    def test_add_customer(self,setup):
        self.driver=setup
        self.lp=Login(self.driver)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.ac=AddCustomer(self.driver)
        self.ac.clickcustomermenu()
        self.logger.info("+++++++++++++++logged into the application++++++++++++++++++")
        self.ac.clickcustomerlist()
        self.ac.clickaddnew()
        email =self.email_generator()
        self.ac.enteremail(email)
        pswd=self.password_generator()
        self.ac.enterpassword(pswd)
        fname=self.fnamegenerator()
        lname=self.lnamegenerator()
        self.ac.enterfname(fname)
        self.ac.enterlname(lname)
        gender=self.gendergenerator()
        self.ac.selectgender(gender)
        self.ac.enterdob("2/23/1990")
        self.ac.entercompname("Qcop")
        self.ac.selecttaxexempt()
        time.sleep(3)
        self.ac.selectnewsletter("Your store name","Test store 2")
        self.ac.setcustomerrole("Registered")
        self.ac.selectmngrvendor("Vendor 1")
        time.sleep(3)
        self.ac.selectactive()
        self.ac.enteradmincomment("added using automation script")
        self.ac.savecustdetails()
        time.sleep(10)
        text=self.driver.find_element(By.XPATH,'//*').text
        # p=re.compile("customer")
        details=list(map(str,(email,fname,lname,pswd,gender)))
        list1=["email","fname","lname","pswd","gender"]
        print(text)
        p=re.compile("The new customer has been added successfully.")
        m=p.findall(text)
        if len(m)!=0:
            assert True
            self.logger.info("the customer with the details {} has been added successfully".format(dict(zip(list1,details))))
        else:
            assert False


