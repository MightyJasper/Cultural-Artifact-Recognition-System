import time
import requests
import os
import io
import hashlib
from PIL import Image
from selenium import webdriver

search_url = "https://instagram.com"
driver_path = "/usr/bin/chromedriver"
wd = webdriver.Chrome(executable_path=driver_path)
# wd.get(search_url)
time.sleep(1)

username = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password = '//*[@id="loginForm"]/div/div[2]/div/label/input'
submit = '//*[@id="loginForm"]/div/div[3]/button'
search_result = '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div[1]/a'
search_input = '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input'
not_now = '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button'

# wd.find_elements_by_xpath(username)[0].send_keys("jizgajizga")
# # wd.find_elements_by_xpath(username).send_keys("abeb")
# wd.find_elements_by_xpath(password)[0].send_keys("843ZwcXGHLdmDP8")
# wd.find_elements_by_xpath(submit)[0].click()
wd.get(os.path.join(search_url,'explore/tags/jebena/'))
# # time.sleep(10)
# wd.find_elements_by_xpath(not_now)[0].click()
image_urls = set()
actual_images = wd.find_elements_by_css_selector('img.FFVAD')
for actual_image in actual_images:
    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
        image_urls.add(actual_image.get_attribute('src'))

for img in image_urls:
    image_content = requests.get(img).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert('RGB')
    # os.getpid()hashlib.sha1(image_content).hexdigest()[:10]
    file_path = os.path.join('./',str(os.getuid()) + '.jpg')
    with open(file_path, 'wb') as f:
        image.save(f, "JPEG", quality=85)
# print(image_urls)
# wd.find_element_by_xpath(search_input)[0].send_keys('#jebena')
# wd.find_element_by_xpath(search_result)[0].click()


# KL4Bh

# //*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div[2]/a
