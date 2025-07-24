import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.TestloginPage import loginPage

import time

import pytest
from selenium import webdriver
#from Pages.loginPage import loginPage
from Test.TestData import ValidPassword, ValidUsername, InvalidUsername, URL

@pytest.fixture
def driver():
    driver= webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def openUrl(driver):
    lPage=loginPage(driver)
    lPage.open(URL)
    time.sleep(1)
    return lPage

# Test Case 1: Valid Login
def test_validCredentials(openUrl):
    openUrl.enterUsername(ValidUsername)
    openUrl.enterPassword(ValidPassword)
    openUrl.clickLogin()
    time.sleep(2)
    assert openUrl.driver.current_url.endswith("/inventory.html")

# Test Case 2: Invalid Login
def test_invalidCredentials(openUrl):
    openUrl.enterUsername(InvalidUsername)
    openUrl.enterPassword(ValidPassword)
    openUrl.clickLogin()
    Error=openUrl.getError()
    time.sleep(1)
    assert Error is not None



