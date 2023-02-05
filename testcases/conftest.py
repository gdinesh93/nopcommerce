from PageObjects.LoginPage import Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.service import Service

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver.exe"))
        print("launching chrome browser")

    elif browser=="firefox":
        opt = Options()
        opt.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver=webdriver.Firefox(service=Service("C:\\Windows\\System32\\geckodriver.exe"),options=opt)
        print("launching firefox browser")

    else:
        driver=webdriver.Edge(service=Service("C:\\Users\\HP\\Downloads\\msedgedriver.exe"))
        print("launching Edge browser")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#it is hook to add environment info to the HTML report
def pytest_configure(config):
    config._metadata['project Name'] = "nopcommerce"
    config._metadata['Module Name'] = "customers"
    config._metadata['Tester'] = "Dinesh"

#it is the hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
