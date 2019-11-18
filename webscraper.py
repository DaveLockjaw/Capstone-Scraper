from selenium.webdriver import Chrome, ActionChains
import pandas as pd
import time

webdriver = r"C:\Users\The Craptop Reborn\chromedriver.exe"
driver = Chrome(webdriver)

url = "https://www.mercari.com/us/category/2/"
driver.get(url)

driver.maximize_window()

# Click on TOPS in Mens category
driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div[7]/div[2]/div/div/button/div/span""").click()

'''
Click on 'View More'
driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/button/p""").click()
'''

driver.implicitly_wait(2)

SCROLL_PAUSE_TIME = 3
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

posts = driver.find_elements_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div/a""")
count = 0
for post in posts:
    print(post.text)
    print()
    count += 1

print(count)
driver.close()

'''
brand = post.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/a/div/div[2]/div[1]/div[1]/div""").text
size = post.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/a/div/div[2]/div[1]/div[1]/p""").text
title = post.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/a/div/div[2]/div[1]/div[2]""").text
price = post.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/a/div/div[2]/div[2]/p""").text

print(brand)
print(size)
print(title)
print(price
'''

'''
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/a[2]""")
action.move_to_element(firstLevelMenu).perform()
HOW TO HOVER
'''