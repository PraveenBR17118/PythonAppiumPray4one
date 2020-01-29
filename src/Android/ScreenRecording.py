'''
Created on 29-Jan-2020

@author: praveen
'''
from appium import webdriver 
import time
import os 
import base64


desrired_cap = {
    "deviceName":"Pixel 3a XL API 29",
    "platformName":"Android",
    "app":"/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/app1-release.apk",
    "appPackage":"com.emf.pray4one"
     }
driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desrired_cap)
driver.implicitly_wait(10)
#Click on start now button  

driver.start_recording_screen()
time.sleep(4)

Strt_bttn = driver.find_element_by_xpath("//android.widget.TextView[@text='START NOW']")
Strt_bttn.click()

eml_fld = driver.find_element_by_xpath("//android.widget.EditText[@text='Email']")
pwd = driver.find_element_by_xpath("//android.widget.EditText[@text='Password']")
lgn_bttn = driver.find_element_by_xpath("//android.widget.TextView[@text='Login']")

eml_fld.send_keys("kehsihbaalkush.89@gmail.com")
pwd.send_keys("Alkush@1991")
lgn_bttn.click()

time.sleep(4)
vid_rawdat = driver.stop_recording_screen()
vid_name = driver.current_activity + time.strftime("%y_%m_%d_%H%M%S")

"""
driver.execute_script('mobile : performEditiorAction' , {'action':'search'})

common action include : go, search, send, next, done, previous 

"""

filepath = os.path.join("/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/Pray4One/ScreenRecording/","opening" +vid_name + ".mp4")
with open (filepath,"wb") as vd:
    vd.write(base64.b64decode(vid_rawdat))