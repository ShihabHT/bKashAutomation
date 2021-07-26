from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from playsound import playsound
import time


driver = webdriver.Chrome('F:\\Tutorial Stuffs\\Python Stuffs\\Browser Drivers\\msedgedriver.exe')

# page = webdriver.Edge('G:\\downloads\\msedgedriver')
driver.get('https://console.firebase.google.com/project/fluid-wallpaper/storage/fluid-wallpaper.appspot.com/files')

driver.find_element_by_id("identifierId").send_keys('')
driver.find_element_by_id("identifierNext").click()
driver.find_element_by_name("password").send_keys('password')
driver.find_element_by_id("passwordNext").click()

driver.find_element_by_xpath('//*[@id="quiz-form"]/div/div/div[1]/div[1]/div/div/div/ul/li[2]/label').click()


