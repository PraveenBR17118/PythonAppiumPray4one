'''
Created on 28-Jan-2020

@author: praveen
'''

from appium import webdriver 



desrired_cap = {
    "deviceName":"Pixel 3a XL API 29",
    "platformName":"Android",
    "app":"/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/AppiumPray4One/app1-release.apk",
    "appPackage":"com.emf.pray4one"
     }
driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desrired_cap)
driver.implicitly_wait(10)

#Click on start now button  

"""
Strt_bttn = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
Strt_bttn.click()

eml_fld = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
pwd = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
lgn_bttn = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView")
eml_fld.send_keys("kehsihbaalkush.89@gmail.com")
pwd.send_keys("Alkush@1991")
lgn_bttn.click()
"""

Strt_bttn = driver.find_element_by_xpath("//android.widget.TextView[@text='START NOW']")
Strt_bttn.click()

eml_fld = driver.find_element_by_xpath("//android.widget.EditText[@text='Email']")
pwd = driver.find_element_by_xpath("//android.widget.EditText[@text='Password']")
lgn_bttn = driver.find_element_by_xpath("//android.widget.TextView[@text='Login']")

eml_fld.send_keys("kehsihbaalkush.89@gmail.com")
pwd.send_keys("Alkush@1991")
lgn_bttn.click()


"""
driver.execute_script('mobile : performEditiorAction' , {'action':'search'})

common action include : go, search, send, next, done, previous 

"""



