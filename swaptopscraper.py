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

url = "https://www.swap.com/shop/mens-apparel/shirts-polos/"
driver.get(url)

driver.maximize_window()

time.sleep(3)

driver.find_element_by_xpath("""//*[@id="close-button"]/a""").click()


def get_post_data():
    count = 0
    SCROLL_PAUSE_TIME = 2
    scrollheight = 400

    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, 400);")

    while True:
        count += 1
        print(count)
        try:
            post = driver.find_element_by_xpath(
                """//*[@id="react"]/div/div[2]/div/div/div/div/div[2]/div[3]/div[1]/div[""" + str(
                    count) + """]""")

        except NoSuchElementException:
            print("No more elements found on page")
            break

        textData = post.text.split('\n')

        # print(post.text)
        print(textData[0])
        try:
            criteria = ["tshirt", "t-shirt", "TSHIRT", "T-Shirt", "Tshirt", "TShirt", "T-shirt", "T-SHIRT", "tshirts",
                        "Tshirts", "TSHIRTS", "t shirt", "T Shirt", "T shirt", "T SHIRT", "t-shirts", "tee", "Tee",
                        "TEE", "tank top", "Tank Top", "TANK TOP", "tanktop", "TankTop", "TANKTOP", "tank",
                        "Tank", "TANK"]
            if any(i in textData[1] for i in criteria):
                continue
            else:
                print(textData[1])
        except IndexError:
            pass
        try:
            print(textData[2])
        except IndexError:
            pass
        try:
            print(textData[3])
        except IndexError:
            pass

        print()

        imgname = randomstring()
        img = driver.find_element_by_xpath(
            """// *[ @ id = "react"] / div / div[2] / div / div / div / div / div[2] / div[3] / div[1] / div[""" + str(
                count) + """] / article / div / a / div[1] / div[1] / div / div / picture / img""")
        src = img.get_attribute('src')

        path = "/Users/The Craptop Reborn/PycharmProjects/Capstone/swaptopimages/"
        if os.path.exists(path) is False:
            os.mkdir(path)
        urllib.request.urlretrieve(src, path + imgname + ".png")

        if count % 24 == 0:
            scrollheight += 2496
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, " + str(scrollheight) + ");")
            print("SCROLLING!")
            print()

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)


get_post_data()
# driver.close()
