from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.keys import Keys
import urllib.request
import random
import string
import pandas as pd
import time


def randomstring(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


webdriver = r"C:\Users\The Craptop Reborn\chromedriver.exe"
driver = Chrome(webdriver)

url = "https://www.mercari.com/us/category/2/"
driver.get(url)

driver.maximize_window()

# Click on Tops in Men's category
driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[7]/div[2]/div/div[1]/button/div/span""").click()

'''
Click on 'View More'
driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/button/p""").click()
'''

driver.implicitly_wait(2)

# USED TO SCROLL TO THE BOTTOM OF THE PAGE. REFERENCED FROM
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
count = 0
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:

    count += 1
    post = driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div["""  + str(count) + """]/a""")
    print(post.text)
    print()
    imgname = randomstring()
    img = driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[""" + str(count) + """]/a/div/div[1]/img""")

    src = img.get_attribute('src')
    urllib.request.urlretrieve(src, r"C:\Users\The Craptop Reborn\PycharmProjects\Capstone\clothingimages" + '\\' + imgname + ".png")
    print(count)

    if count % 72 == 0:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

driver.close()
