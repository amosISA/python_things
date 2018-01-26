from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time 

driver = webdriver.Chrome('C:\Users\AMOS\Downloads\selenium\chromedriver')
driver.get("http://subvenciones.amosdev.eu")

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.clear()
password.clear()
submit = driver.find_element_by_tag_name('button')
username.send_keys("ayuntamiento")
password.send_keys("subvenciones12345")

try:
	submit.click()
except WebDriverException:
	print "Element is not clickable"

time.sleep(3)
driver.close()