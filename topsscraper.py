from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import random
import string
import pandas as pd
import time
import os


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
driver.find_element_by_xpath("""//*[@id="__next"]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[8]/div[2]/div/div[1]/button/div""").click()

# USED TO SCROLL TO THE BOTTOM OF THE PAGE. REFERENCED FROM
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
count = 0
SCROLL_PAUSE_TIME = 1
scrollheight = 160

time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, 160);")

while True:

    count += 1
    print(count)
    try:
        post = driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[""" + str(count) + """]/a""")
    except NoSuchElementException:
        print("No more elements found on page")
        break

    print(post.text)
    print()
    imgname = randomstring()
    img = driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[""" + str(count) + """]/a/div/div[1]/img""")
    src = img.get_attribute('src')

    path = "/Users/The Craptop Reborn/PycharmProjects/Capstone/topimages/"
    if os.path.exists(path) is False:
        os.mkdir(path)
    urllib.request.urlretrieve(src, path + imgname + ".png")

    if count % 18 == 0:
        scrollheight += 894
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, " + str(scrollheight) + ");")
        print("SCROLLING!")
        print()

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

driver.close()

'''
Click on 'View More'
driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/button/p""").click()
'''
