from PageObjects.LoginPage import Login
import pytest
from utilities.readproperties import Readconfig
from utilities.customlogger import Loggen

class Test_001_login:
    baseurl=Readconfig.getapplicationurl()
    email_username=Readconfig.getusername()
    password=Readconfig.getpassword()
    logger=Loggen.log()

    @pytest.mark.regrerssion
    def test_homepagetitle(self,setup):
        self.logger.info("*******Test_001_login*********")
        self.logger.info("******Verifying Home page title********")

        self.driver= setup
        self.driver.get(self.baseurl)
        act_title="Your store. Login"
        if self.driver.title==act_title:
            assert  True
            self.driver.close()
            self.logger.info("***********home page title is passed*************")
        else:
            self.driver.close()
            self.logger.error("************home page title is failed***************")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*******verifying Login test*********")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.lp=Login(self.driver)
        self.lp.setusername(self.email_username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title="Dashboard / nopCommerce administration"
        if self.driver.title==act_title:
            assert True
            self.logger.info("*******Login test is passed*********")

            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\nopcommerce\\screenshots\\loginpage.jpg")
            self.driver.close()
            self.logger.error("*******login test is failed*********")

            assert False, "dashboard title not matched"
