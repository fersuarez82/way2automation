from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


@given('launch chrome browser')
def launchBrowser(self):
    self.driver = webdriver.Chrome('../../chromedriver.exe')
    self.driver.implicitly_wait(10)


@when('open way2automation page')
def openHomePage(self):
    self.driver.get("https://www.way2automation.com/angularjs-protractor/webtables/")


@when('add a user')
def addUser(self):
    self.driver.find_element(By.XPATH, "//button[@class='btn btn-link pull-right']").click()
    self.driver.find_element(By.XPATH, "//input[@name='FirstName']").send_keys("Fernando")
    self.driver.find_element(By.XPATH, "//input[@name='LastName']").send_keys("Suarez")
    self.driver.find_element(By.XPATH, "//input[@name='UserName']").send_keys("fersua")
    self.driver.find_element(By.XPATH, "//input[@name='Password']").send_keys("101082")
    self.driver.find_element(By.XPATH, "// label[@class ='radio ng-scope ng-binding']").click()
    select = Select(self.driver.find_element(By.XPATH, "//select[@name='RoleId']"))
    select.select_by_visible_text('Customer')
    self.driver.find_element(By.XPATH, "//input[@name='Email']").send_keys("fersua@yahoo.com")
    self.driver.find_element(By.XPATH, "//input[@name='Mobilephone']").send_keys("1137055404")
    self.driver.find_element(By.XPATH, "// button[@class ='btn btn-success']").click()
    time.sleep(2)


@then('validate added user')
def validate(self):
    userAdded = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td[1]")
    textUser = userAdded.text
    assert(textUser == "Fernando")
    time.sleep(2)


@then('close browser')
def closeBrowser(self):
    self.driver.close()
