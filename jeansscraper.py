from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import random
import string
import time
import os
import boto3
from botocore.exceptions import NoCredentialsError


def randomstring(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def put_listing(textData, listing_id):
    table.put_item(
        Item={
            'listing_id': listing_id,
            'title': textData[0],
            'designer': textData[1],
            'category': 'Jeans',
            'size': textData[3],
            'price': textData[4]
        }
    )
    
def upload_to_aws(local_file, s3_file_name):
    BUCKET = 'lowballimages'

    s3 = boto3.client('s3', aws_access_key_id='AKIAJMS6MK2EDRKO3DUQ', aws_secret_access_key='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', region_name='us-east-2')

    try:
        s3.upload_file(local_file, BUCKET, s3_file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

ddb = boto3.resource('dynamodb', aws_access_key_id='AKIAJMS6MK2EDRKO3DUQ', aws_secret_access_key='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', region_name='us-east-2')
table = ddb.Table('listings')

webdriver = r"C:\Users\grigg\chromedriver.exe"#C:\Users\The Craptop Reborn\chromedriver.exe"
driver = Chrome(webdriver)

url = "https://www.mercari.com/us/category/2/"
driver.get(url)

driver.maximize_window()

# Click on Jeans in Men's category
driver.find_element_by_xpath("""//*[@id="__next"]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[8]/div[2]/div/div[4]/button/div""").click()

# USED TO SCROLL TO THE BOTTOM OF THE PAGE. REFERENCED FROM
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
count = 0
SCROLL_PAUSE_TIME = 5
scrollheight = 210

time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, 210);")

while True:

    count += 1
    print(count)
    try:
        post = driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[""" + str(count) + """]/a""")
    except NoSuchElementException:
        print("No more elements found on page")
        break
    
    randomId = randomstring()
    print(post.text)
    tempData = post.text.split('\n')
    put_listing(tempData, randomId)
    
    print()
    img = driver.find_element_by_xpath("""//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[""" + str(count) + """]/a/div/div[1]/img""")
    src = img.get_attribute('src')

    path = "C:/Users/grigg/OneDrive/Desktop/Capstone/jeanimages"#"/Users/The Craptop Reborn/PycharmProjects/Capstone/jeanimages/"
    if os.path.exists(path) is False:
        os.mkdir(path)
    urllib.request.urlretrieve(src, path + randomId + ".png")
    upload_to_aws((path + randomId + ".png"), randomId)
    
    if count % 8 == 0:
        scrollheight += 914
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, " + str(scrollheight) + ");")
        print("SCROLLING!")
        print()

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

driver.close()

