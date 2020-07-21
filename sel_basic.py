from selenium import webdriver 
import time
from selenium.webdriver import ActionChains
# giving path of rxe to the driver
path = 'C:\\python\\jarvis\\chromedriver.exe'

# giving path to the driver
driver = webdriver.Chrome(path)

# opening the search results 
driver.get('http://idhrudhr.tk/')

# quiting the last opened tab
# driver.close()

# quiting the browser
# driver.quit()

# getting the links from the page
# links = driver.find_elements_by_tag_name('a')
# # print(links)
# time.sleep(2)

# for link in links:
#     print(link.text)

# 

# # tabs = driver.current_handle {it prints all the tabs in thee window }
# # to switch bt tabs use
# driver.switch_to.window(tab) {which ever tab we want anfd also loops can be used to loop throung the tabs}

# driver.current_url {for printitng the current current_url}
# driver.tittle {for printing the titlw of the page}

# 

# {{MOUSE HOVERING EFFET}} 

# gallery = driver.find_element_by_xpath(
#     '//*[@id="navbarSupportedContent"]/ul/li[4]/a')
# gallery.click()
# time.sleep(5)

# img = driver.find_element_by_xpath('/html/body/section/div/div[2]/div[1]/div/div')
# actions = ActionChains(driver)
# actions.move_to_element(img).perform()

# similarly dounle click and right click drag drop and many more can also be done using
# actions.double_click() double click
# actions.context_click() right click

# {{PLAYING WITH THE WINDOW SCREEN}}
# 1 MAXIMISE
# time.sleep(1)
driver.maximize_window()
# time.sleep(5)
# {{2 scrolling down by pixel }}
# driver.execute_script("window.scrollBy(0,1000)","")

# {{3 SCROLL UPTO DOWN THE PAGE}}
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# #  {{4 scroll untill an element is found}}
# about = driver.find_element_by_xpath('//*[@id="abs"]/div/div[1]/div[2]/h1')
# driver.execute_script('arguments[0].scrollIntoView();',about)


# Taking screnshots
driver.save_screenshot('C:\python\jarvis\Selenium\screenshot.png')
