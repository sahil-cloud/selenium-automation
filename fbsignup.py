from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

path = 'C:\\python\\jarvis\\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://www.facebook.com/')
# time.sleep(2)

# filling the input part of the form
fname = driver.find_element_by_id('u_0_m')
fname.send_keys("name")
lname = driver.find_element_by_id('u_0_o')
lname.send_keys("lname")
phone = driver.find_element_by_id('u_0_r')
phone.send_keys('phine")
password = driver.find_element_by_id('password_step_input')
password.send_keys("pass")

# selecting gender using isselect method
# for male selection
gender = driver.find_element_by_id('u_0_7')
verify_gender = gender.is_selected()
print(verify_gender)

if(verify_gender != True):
    gender.click()

# filling the bday
# we use select coz the options are fetching from the select tag
date = Select(driver.find_element_by_id('day'))

date.select_by_value('9')

month = Select(driver.find_element_by_id('month'))
month.select_by_value('5')

year = Select(driver.find_elements_by_id('year'))
year.select_by_value('2000')


