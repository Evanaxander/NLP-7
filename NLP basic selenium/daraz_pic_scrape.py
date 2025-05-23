from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os


driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/mens-sports-socks/lotto/')
driver.maximize_window()


time.sleep(5)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  


image_elements = driver.find_elements(By.XPATH, '//img[contains(@class, "image")]')


os.makedirs('daraz_images', exist_ok=True)


for index, img in enumerate(image_elements):
    img_url = img.get_attribute('src') or img.get_attribute('data-src')
    if img_url:
        try:
            img_data = requests.get(img_url).content
            with open(f'daraz_images/image_{index + 1}.jpg', 'wb') as handler:
                handler.write(img_data)
            print(f'Downloaded: image_{index + 1}.jpg')
        except Exception as e:
            print(f"Failed to download image {index + 1}: {e}")

time.sleep(20)
driver.quit()
