'''
Created on 28-Jan-2020

@author: praveen
'''

from appium import webdriver 

"""desrired_cap = {
    "deviceName":"emulator-5554",
    "platformName":"Android",
    "app":"/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/app1-release.apk"
     }
"""

desrired_cap = {
    "deviceName":"Pixel 3a XL API 29",
    "platformName":"Android",
    "app":"/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/app1-release.apk"
     }
driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desrired_cap)