import time

import pytest

from utilities.xlutilities import *
from utilities.readproperties import Readconfig
from PageObjects.LoginPage import Login
from utilities.customlogger import Loggen
class Test_001_login_ddt:
    baseurl = Readconfig.getapplicationurl()
    path = r"C:\Users\HP\PycharmProjects\nopcommerce\testdata\logindata.xlsx"
    logger = Loggen.log()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********Test_001_login_ddt********")
        self.logger.info("*********Starting test_login_ddt******")

        self.driver=setup
        self.lp=Login(self.driver)

        self.row=getrowcount(self.path,"Sheet1")
        self.col=getcolumncount(self.path,"Sheet1")
        self.logger.info("*********collected the data from the file******")

        self.ls=[]
        for r in range(2,self.row+1):
            self.username=readdata(self.path,"Sheet1",r,1)
            self.password=readdata(self.path,"Sheet1",r,2)
            self.exp=readdata(self.path,"Sheet1",r,3)
            self.driver.get(self.baseurl)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(3)
            act_title="Dashboard / nopCommerce administration"
            if self.driver.title==act_title:
                self.logger.info("*********logged into the application******")

                self.lp.clicklogout()
                if self.exp=="pass":
                    self.logger.info("*********logged into the application using the correct details******")

                    self.ls.append("pass")
                    writedata(self.path,"Sheet1",r,4,"pass")
                else:
                    self.logger.info("*********login passed with invalid credentials*******")

                    self.ls.append("fail")
                    writedata(self.path,"Sheet1",r,4,"fail")

            elif self.driver!=act_title:
                if self.exp=="pass":
                    self.logger.info("********negative testing passed*********")

                    self.ls.append("fail")
                    writedata(self.path,"Sheet1",r,4,"fail")

                else:
                    self.logger.info("*********negative testing failed********")

                    self.ls.append("pass")
                    writedata(self.path,"Sheet1",r,4,"fail")


        print("the test results are",self.ls)

        if "fail" not in self.ls:
            assert True
            self.logger.info("********The login_ddt test passed***********")

        else:
            self.logger.error("*********The login_ddt test failed*********")
            assert False




