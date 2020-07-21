from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains
# giving path of rxe to the driver
path = 'C:\\python\\jarvis\\chromedriver.exe'

# giving path to the driver
driver = webdriver.Chrome(path)

# opening the search results 
driver.get('http://idhrudhr.tk/login.php')


# login into the account
email = driver.find_element_by_xpath('/html/body/section/div[2]/form/input[1]')
password = driver.find_element_by_xpath('/html/body/section/div[2]/form/input[2]')

btn_Send = driver.find_element_by_xpath('/html/body/section/div[2]/form/button[1]')

email.clear()
email.send_keys('email')
password.clear()
password.send_keys('pass')
btn_Send.click()

sleep(5)
driver.switch_to_alert().accept()
driver.switch_to_alert().accept()
sleep(5)

# filling the booking form
fromd = driver.find_element_by_xpath('/html/body/section[1]/div[2]/form/input[1]')
tod = driver.find_element_by_xpath('/html/body/section[1]/div[2]/form/input[2]')
address = driver.find_element_by_xpath('/html/body/section[1]/div[2]/form/input[3]')
time = driver.find_element_by_xpath('/html/body/section[1]/div[2]/form/input[4]')

btn_book = driver.find_element_by_xpath('/html/body/section[1]/div[2]/form/a/button')

fromd.send_keys('20-07-2020')
tod.send_keys('21-07-2020')
address.send_keys('jhalrapatan rajasthan')
time.send_keys('10:00')
btn_book.click()

# booking the car
btn_book1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/form/input[2]')
btn_book1.click()

# sleep(5)
# btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/form')
# btn.submit()
# btn.send_keys('Select')
# btn.send_keys(Keys.RETURN)
sleep(5)
btn_b = driver.find_element_by_xpath('/html/body/section[1]/div/form/button')
btn_b.click()
sleep(3)
driver.switch_to_alert().accept()
driver.switch_to_alert().accept()
sleep(5)

# logout
logout = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a[2]')
logout.click()
