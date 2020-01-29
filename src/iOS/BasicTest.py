'''
Created on 29-Jan-2020

@author: praveen
'''
from appium import webdriver 

desrired_cap = {
  "platformName": "iOS",
  "app": "/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/Pray4One 2.zip",
  "deviceName": "iPhone XR",
  "platformVersion": "12.1",
  "automationName": "appium"
  }
driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desrired_cap)
