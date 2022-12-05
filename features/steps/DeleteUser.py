from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('launch chrome browser1')
def launchBrowser(self):
    self.driver = webdriver.Chrome('../../chromedriver.exe')
    self.driver.implicitly_wait(10)


@when('open way2automation page1')
def openHomePage(self):
    self.driver.get("https://www.way2automation.com/angularjs-protractor/webtables/")


@when('user novak exists')
def validate(self):
    userDelete = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td[3]")
    textUser1 = str(userDelete.text)
    assert (textUser1 == "novak")
    time.sleep(2)

@when('delete user novak')
def User(self):
    self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td[11]/button/i").click()
    self.driver.find_element(By.XPATH, "//button[@class='btn ng-scope ng-binding btn-primary']").click()
    time.sleep(2)


@then('validate deleted user')
def validate(self):
    userDeleted = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td[3]")
    textUser2 = userDeleted.text
    assert(textUser2 != "novak")
    time.sleep(2)


@then('close browser1')
def closeBrowser(self):
    self.driver.close()

