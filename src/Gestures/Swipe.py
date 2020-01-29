'''
Created on 29-Jan-2020

@author: praveen
'''
from appium import webdriver 
import time
#from appium.webdriver.common.touch_action import TouchAction

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

eml_fld.send_keys("praveenbr@enwidth.com")
pwd.send_keys("PRK@1718")
lgn_bttn.click()

time.sleep(10)

pray4me = driver.find_element_by_xpath("//android.widget.TextView[@text ='Pray4me']")
pray4me.click()

time.sleep(5)

"""
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#Element = driver.find_element_by_xpath("//android.widget.TextView[@text='Submit']")

#driver.execute_script("arguments[0].scrollIntoView();",Element)

#driver.execute_script("mobile: scroll", {"direction": "down"})

#driver.execute_script('mobile: scroll', {"element": Element, "toVisible": True})

#driver.swipe(470, 1400, 470, 1000, 400)

action = TouchAction(driver)
el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Submit']")))
action.press(el).move_to(x=10, y=-500).release().perform()

Element = driver.find_element_by_id("e96ec98c-0e94-43a9-9b90-416effea428d")

actions = TouchAction(driver)
actions.scroll_from_element(Element, 10, 100)
actions.scroll(10, 100)
actions.perform()

el1 = driver.find_element_by_xpath("//android.widget.TextView[@text='Choose Category']")
el2 = driver.find_element_by_xpath("//android.widget.EditText[@text='Email']")

action = TouchAction(driver)
action.press(el1).move_to(el2).release().perform()

el = driver.find_element_by_xpath("//android.widget.EditText[@text='Email']")
driver.execute_script("mobile: scroll", {"direction": 'down', 'element': el}) 

driver.execute_script("mobile: scroll", {'direction': 'down'})
"""
el = driver.find_element_by_xpath("//android.widget.EditText[@text='Submit']")
driver.execute_script("mobile: scroll", {"direction": 'down', 'element': el})



