from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Ryan")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Guide")
email = driver.find_element_by_name("email")
email.send_keys("gudiedryan@gmail.com")
email.send_keys(Keys.ENTER)