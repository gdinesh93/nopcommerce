import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SearchCustomer:
    txtbox_emai_xpath='//*[@name="SearchEmail"]'
    txtbox_fname_xpath='//*[@name="SearchFirstName"]'
    txtbox_lname_xpath='//*[@name="SearchLastName"]'
    btn_search_xpath='//*[@id="search-customers"]'
    tbl_search_result_xpath='//*[@id="customers-grid"]'
    tbl_row_xpath='//*[@id="customers-grid"]/tbody/tr'
    tbl_column_xpath='//*[@class="dataTables_scrollHeadInner"]//th'
    tbl_data_xpath='//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver.exe"))


    def xploc(self,loc):
        p=self.driver.find_element(By.XPATH,loc)
        return p

    def enteremail(self,email):
        self.xploc(self.txtbox_emai_xpath).send_keys(email)

    def enterfname(self,fname):
        self.xploc(self.txtbox_fname_xpath).send_keys(fname)

    def enterlname(self,lname):
        self.xploc(self.txtbox_lname_xpath).send_keys(lname)

    def getnoofrows(self):
        return len(self.driver.find_elements(By.XPATH,self.tbl_row_xpath))

    def getnoofcolumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tbl_column_xpath))

    def searchbyEmail(self,email):
        flag=True
        act=ActionChains(self.driver)
        ele = self.driver.find_element(By.XPATH, '//*[text()="nopCommerce"]')
        act.scroll_to_element(ele).perform()
        time.sleep(3)
        for r in range(1,self.getnoofrows()+1):
            self.act_email=self.xploc('//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[2]').text
            if self.act_email==email:
                flag=False
                break

        return flag

    def searchbyname(self,name):
        flag = True
        act=ActionChains(self.driver)
        ele = self.driver.find_element(By.XPATH, '//*[text()="nopCommerce"]')
        act.scroll_to_element(ele).perform()
        try:
            for r in range(1, self.getnoofrows() + 1):
                self.act_name = self.xploc('//*[@id="customers-grid"]/tbody/tr[' + str(r) + ']/td[3]').text
                if self.act_name ==name:
                    flag = False
                    break
        except:
            pass

        finally:
            return flag

    def clicksearch(self):
        self.xploc(self.btn_search_xpath).click()


