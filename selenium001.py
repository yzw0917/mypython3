import time,os
from selenium import webdriver
# import unittest
#from selenium.common.exceptions import NoSuchAttributeException
#from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
#browser.implicitly_wait(10)
browser.maximize_window()
#time.sleep(3)
browser.get("https://www.baidu.com/")
print ("浏览器打开成功")
# print (browser.page_source)
print (browser.current_url)
print (browser.current_window_handle)
print (browser.get_cookies())
time.sleep(300)
browser.quit()