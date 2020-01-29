'''
Created on 29-Jan-2020

@author: praveen
'''
from appium import webdriver 
import time

desrired_cap = {
    "deviceName":"Pixel 3a XL API 29",
    "platformName":"Android",
    "app":"/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/app1-release.apk",
    "appPackage":"com.emf.pray4one",
    "newConnectionTimeout" : 60,
     }
driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desrired_cap)
driver.implicitly_wait(10)

Strt_bttn = driver.find_element_by_xpath("//android.widget.TextView[@text='START NOW']")
Strt_bttn.click()

eml_fld = driver.find_element_by_xpath("//android.widget.EditText[@text='Email']")
pwd = driver.find_element_by_xpath("//android.widget.EditText[@text='Password']")
lgn_bttn = driver.find_element_by_xpath("//android.widget.TextView[@text='Login']")

eml_fld.send_keys("kehsihbaalkush.89@gmail.com")
pwd.send_keys("Alkush@1991")
lgn_bttn.click()

ts = time.strftime("%d %m %y %H%M%S")
acti = driver.current_activity
file_name = acti + ts
driver.save_screenshot("/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/Pray4One/Screenshot/"+"loginpage"+file_name+".png" )