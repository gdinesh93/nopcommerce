import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    lnk_customer_menu_xpath='//p[contains(text(),"Promotions")]/preceding::p[contains(text(),"Customers")]'
    lnk_customer_menu_list_xpath='//*[@href="/Admin/Customer/List"]/p[contains(text(),"Customers")]'
    btn_add_new_xpath='//*[@href="/Admin/Customer/Create"]'
    txtbox_email_xpath='//*[@name="Email"]'
    txtbox_password_xpath='//*[@name="Password"]'
    txtbox_fname_xpath='//*[@id="FirstName"]'
    txtbox_lname_xpath='//*[@name="LastName"]'
    rdbtn_male_xpath='//*[contains(text(),"Male")]'
    rdbtn_female_xpath='//*[contains(text(),"Female")]'
    txtbox_dob_xpath='//*[@id="DateOfBirth"]'
    txtbox_company_xpath='//*[@id="Company"]'
    checkbox_tax_exempt_xpath='//*[@id="IsTaxExempt"]'
    txtbox_newsletter_xpath='//*[@class="k-multiselect-wrap k-floatwrap"]'
    list_yourstore_xpath='//li[text()="Your store name"]'
    list_teststore2_xpath='//li[contains(text(),"Test")]'
    txtbox_customerroles_xpath='//*[@id="SelectedCustomerRoleIds_taglist"]/parent::div'
    list_administrators_xpath='//li[text()="Administrators"]'
    list_forummoderator_xpath='//li[text()="Forum Moderators"]'
    list_guest_xpath='//li[text()="Guests"]'
    list_registered_xpath='//li[text()="Registered"]'
    list_vendors_xpath='//li[text()="Vendors"]'
    select_managerOfVendor_xpath='//*[@id="VendorId"]'
    checkbox_active_xpath='//*[@id="Active"]'
    txtbox_admincomment_xpath='//*[@name="AdminComment"]'
    btn_register_close_xpath='//*[text()="Registered"]/following::span[@title="delete"]'
    btn_save_xpath='//*[@name="save"]'

    def __init__(self, driver):
        self.driver=driver
        # self.driver=webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver.exe"))

    def xpathlocator(self,locator):
        return self.driver.find_element(By.XPATH,locator)

    def clickcustomermenu(self):
        self.xpathlocator(self.lnk_customer_menu_xpath).click()

    def clickcustomerlist(self):
        self.xpathlocator(self.lnk_customer_menu_list_xpath).click()

    def clickaddnew(self):
        self.xpathlocator(self.btn_add_new_xpath).click()

    def enteremail(self,email):
        self.xpathlocator(self.txtbox_email_xpath).send_keys(email)

    def enterpassword(self,password):
        self.xpathlocator(self.txtbox_password_xpath).send_keys(password)

    def enterfname(self,fname):
        self.xpathlocator(self.txtbox_fname_xpath).send_keys(fname)

    def enterlname(self,lname):
        self.xpathlocator(self.txtbox_lname_xpath).send_keys(lname)

    def selectgender(self,gender):
        if gender.lower()=="male":
            self.xpathlocator(self.rdbtn_male_xpath).click()
        elif gender.lower()=="female":
            self.xpathlocator(self.rdbtn_female_xpath).click()

    def enterdob(self,dob):
        self.xpathlocator(self.txtbox_dob_xpath).send_keys(dob)

    def entercompname(self,cname):
        self.xpathlocator(self.txtbox_company_xpath).send_keys(cname)

    def selecttaxexempt(self):
        self.xpathlocator(self.checkbox_tax_exempt_xpath).click()

    def selectnewsletter(self,b,a=None):
        if b=="Your Store Name":
            self.xpathlocator(self.txtbox_newsletter_xpath).click()
            self.xpathlocator(self.list_yourstore_xpath)
        elif b=="Test Store 2":
            self.xpathlocator(self.txtbox_newsletter_xpath).click()
            self.xpathlocator(self.list_teststore2_xpath).click()
        if a!=None and b!=None:
            self.xpathlocator(self.txtbox_newsletter_xpath).click()
            self.xpathlocator(self.list_yourstore_xpath).click()
            time.sleep(2)
            act = ActionChains(self.driver)
            ele=self.xpathlocator(self.txtbox_admincomment_xpath)
            act.scroll_to_element(ele).perform()
            self.xpathlocator(self.txtbox_newsletter_xpath).click()
            self.xpathlocator(self.list_teststore2_xpath).click()

    def setcustomerrole(self,role):
        if role!="Registered":
            self.xpathlocator(self.btn_register_close_xpath).click()

            if role=="Forum Moderators":
                self.xpathlocator(self.txtbox_customerroles_xpath).click()
                list_item=self.xpathlocator(self.list_forummoderator_xpath)
            elif role=="Administrators":
                self.xpathlocator(self.txtbox_customerroles_xpath).click()
                list_item=self.xpathlocator(self.list_administrators_xpath)
            elif role=="Vendors":
                self.xpathlocator(self.txtbox_customerroles_xpath).click()
                list_item=self.xpathlocator(self.list_vendors_xpath)
            elif role=="Guests":
                self.xpathlocator(self.txtbox_customerroles_xpath).click()
                list_item=self.xpathlocator(self.list_guest_xpath)


            self.driver.execute_script("arguments[0].click();",list_item)

        else:
            pass

    def selectmngrvendor(self,value):
        drp=Select(self.xpathlocator(self.select_managerOfVendor_xpath))
        drp.select_by_visible_text(value)


    def selectactive(self):
        check=self.driver.find_element(By.XPATH,self.checkbox_active_xpath)
        if check.is_selected():
            pass
        else:
            check.click()

    def enteradmincomment(self,comment):
        self.xpathlocator(self.txtbox_admincomment_xpath).send_keys(comment)

    def savecustdetails(self):
        self.xpathlocator(self.btn_save_xpath).click()
