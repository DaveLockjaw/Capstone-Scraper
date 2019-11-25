from selenium.webdriver import Chrome
import time

webdriver = r"C:\Users\The Craptop Reborn\chromedriver.exe"
driver = Chrome(webdriver)

url = "https://www.mercari.com/us/category/2/"
driver.get(url)

driver.maximize_window()

# Click on Sweats & hoodies in Men's category
driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[7]/div[2]/div/div[2]/button/div/span""").click()

driver.implicitly_wait(2)

# USED TO SCROLL TO THE BOTTOM OF THE PAGE. REFERENCED FROM
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
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
