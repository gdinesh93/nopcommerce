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
from PageObjects.SearchCustomer import SearchCustomer

class Test_004_search_customer:
    baseurl=Readconfig.getapplicationurl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    logger=Loggen.log()

    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.driver=setup
        self.lp=Login(self.driver)
        self.sc=SearchCustomer(self.driver)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.ac=AddCustomer(self.driver)
        self.ac.clickcustomermenu()
        self.ac.clickcustomerlist()
        email="brenda_lindgren@nopCommerce.com"
        self.sc.enteremail(email)
        self.sc.clicksearch()
        self.sc.searchbyEmail(email)
        if self.sc.act_email=="brenda_lindgren@nopCommerce.com":
            assert True
            self.logger.info("+++++Search customer by email passed+++++++")
            self.driver.close()
        else:
            print(self.sc.act_email)

            self.logger.info("++++++Search customer by email failed++++")
            self.driver.close()
            assert False
    @pytest.mark.regression
    def test_search_customer_by_name(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.sc = SearchCustomer(self.driver)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.ac = AddCustomer(self.driver)
        self.ac.clickcustomermenu()
        self.ac.clickcustomerlist()
        self.sc.enterfname("Virat")
        self.sc.enterlname("kohli")
        self.sc.clicksearch()
        if self.sc.searchbyname("Virat Kohli")==True:
            print(self.sc.act_name)

            assert True
            self.logger.info("++++Search by name test passed+++")

        else:
            self.logger.info("++++Search by customer name failed++++++")
            print(self.sc.act_name)

