import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from playsound import playsound
import time


# 166, 322
# 166, 380
# 166, 432
# 166, 488

# while True:
page = webdriver.Chrome('F:\\Tutorial Stuffs\\Python Stuffs\\Browser Drivers\\chromedriver.exe')
# page = webdriver.Edge('G:\\downloads\\msedgedriver')
page.get('https://bkash.com/quiz/public/')

search = page.find_element_by_name('phone')
search.send_keys('01712457812')
page.find_element_by_id('checkbox').click()
search.send_keys(Keys.ENTER)

# page.implicitly_wait(5)
time.sleep(1)

page.find_element_by_xpath('//*[@id="quiz-form"]/div/div/div[1]/div[1]/div/div/div/ul/li[2]/label').click()
page.find_element_by_xpath('//*[@id="quiz-form"]/div/div/div[1]/div[2]/div/div/div/ul/li[3]/label').click()
page.find_element_by_xpath('//*[@id="quiz-form"]/div/div/div[1]/div[3]/div/div/div/ul/li[1]/label').click()

# for x in range(3):
#     y = random.randint(1, 4)
#     if y == 1:
#         pyautogui.click(166, 322)
#     elif y == 2:
#         pyautogui.click(166, 380)
#     elif y == 3:
#         pyautogui.click(166, 432)
#     else:
#         pyautogui.click(166, 488)


# page.find_element_by_class_name('seconds').text

time.sleep(15)

timeTaken = page.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/h4/span').text
print(timeTaken)
result = page.find_element_by_class_name('result').text
print(result)
if result == '3':
    print("Mission successful")
    playsound('data_upload_complete.wav')
    # break
else:
    print("Mission failed..")

page.quit()