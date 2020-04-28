from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import random
import string
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
driver.find_element_by_xpath(
    """//*[@id="__next"]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[8]/div[2]/div/div/button""").click()


# USED TO SCROLL TO THE BOTTOM OF THE PAGE. REFERENCED FROM
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python


def get_post_data():
    count = 0
    SCROLL_PAUSE_TIME = 2
    scrollheight = 210

    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, 210);")

    while True:

        count += 1
        print(count)
        try:
            post = driver.find_element_by_xpath(
                """//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[""" + str(
                    count) + """]/a""")
        except NoSuchElementException:
            print("No more elements found on page")
            break

        textData = post.text.split('\n')

        # print(post.text)
        if textData[2] == " | ":
            try:
                criteria = ["tshirt", "t-shirt", "TSHIRT", "T-Shirt", "Tshirt", "TShirt", "T-shirt", "T-SHIRT", "tshirts",
                            "Tshirts", "TSHIRTS", "t shirt", "T Shirt", "T shirt", "T SHIRT", "t-shirts", "tee", "Tee",
                            "TEE", "tank top", "Tank Top", "TANK TOP", "tanktop", "TankTop", "TANKTOP", "tank",
                            "Tank", "TANK"]
                if any(i in textData[0] for i in criteria):
                    continue
                else:
                    print(textData[0])
            except IndexError:
                pass
            try:
                print(textData[1])
            except IndexError:
                pass
            try:
                print(textData[3])
            except IndexError:
                pass
            try:
                print(textData[4])
            except IndexError:
                pass
        else:
            try:
                print(textData[0])
            except IndexError:
                pass
            try:
                print(textData[1])
            except IndexError:
                pass
            try:
                print(textData[2])
            except IndexError:
                pass

        print()

        imgname = randomstring()
        img = driver.find_element_by_xpath(
            """//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[""" + str(
                count) + """]/a/div/div[1]/div/img""")

        src = img.get_attribute('src')

        path = "/Users/The Craptop Reborn/PycharmProjects/Capstone/topimages/"
        if os.path.exists(path) is False:
            os.mkdir(path)
        urllib.request.urlretrieve(src, path + imgname + ".png")

        if count % 18 == 0:
            scrollheight += 909
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, " + str(scrollheight) + ");")
            print("SCROLLING!")
            print()

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)


get_post_data()
# driver.close()

'''
Click on 'View More'
driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/button/p""").click()
'''
