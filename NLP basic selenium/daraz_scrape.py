from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.bd/mens-sports-socks/lotto/')

driver.maximize_window()



title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[5]/div/div/div[1]/div/a/div/img').img

link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[5]/div/div/div[1]/div/a/div/img').get_attribute('src')

print(title,link)

time.sleep(20)