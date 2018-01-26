from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time 

# while True:
	# driver = webdriver.Chrome('C:\Users\AMOS\Downloads\selenium\chromedriver') 
	# driver.get("http://www.python.org")
	# assert "Python" in driver.title
	# elem = driver.find_element_by_name("q")
	# elem.clear()
	# elem.send_keys("pycon")
	# elem.send_keys(Keys.RETURN)
	# assert "No results found." not in driver.page_source
	# driver.close()

while True: 
	driver = webdriver.Chrome('C:\Users\AMOS\Downloads\selenium\chromedriver')
	driver.get("http://www.xn--votamonopolyespaa-uxb.com/vota.php?id=3790")

	# get button and change class to whatever 
	button_vote_form = driver.find_element_by_css_selector('button.o-cards-btnVota')
	driver.execute_script("arguments[0].setAttribute('class','vote-link up voted')", button_vote_form)

	try:
		button_vote_form.click()
	except WebDriverException:
		print "Element is not clickable"

	time.sleep(3)
	driver.close()