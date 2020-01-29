'''
Created on 29-Jan-2020

@author: praveen
'''

from appium import webdriver 
import time

desrired_cap = {
  "platformName": "iOS",
  "app": "/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/Pray4One 2.zip",
  "deviceName": "iPhone XR",
  "platformVersion": "12.1",
  "automationName": "appium"
  }
driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desrired_cap)
driver.implicitly_wait(10)

Strt_bttn = driver.find_element_by_xpath("(//XCUIElementTypeOther[@name='START NOW'])[11]")
Strt_bttn.click()

eml_fld = driver.find_element_by_xpath("(//XCUIElementTypeOther[@name='Email'])[3]/XCUIElementTypeTextField")
pwd = driver.find_element_by_xpath("(//XCUIElementTypeOther[@name='Password'])[3]/XCUIElementTypeSecureTextField")
lgn_bttn = driver.find_element_by_xpath("//XCUIElementTypeOther[@name='Login']")

eml_fld.send_keys("kehsihbaalkush.89@gmail.com")
pwd.send_keys("Alkush@1991")
time.sleep(4)
lgn_bttn.click()
time.sleep(4)
print(lgn_bttn.is_enabled())
lgn_bttn.click()
time.sleep(8)

all_logo = driver.find_element_by_id("B6000000-0000-0000-BB09-000000000000").get_attribute()
print(all_logo)
