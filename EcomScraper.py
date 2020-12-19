# Web Scraping
#reference
'''
https://medium.com/@zfwong.wilson/web-scraping-e-commerce-sites-to-compare-prices-with-python-part-1-360509ee5c62
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
Lazada_url = 'https://www.lazada.com.my'
search_item = 'Nescafe Gold refill 170g' 


# Select custom Chrome options
# to block unncesseary ads etc
options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')


# open the chrome browser
driver = webdriver.Chrome(PATH)
driver.get(Lazada_url)
print(driver.title)


# look at html inspect. find search button element
search = driver.find_element_by_id('q')
search.send_keys(search_item)
search.send_keys(Keys.RETURN)



'''
#- single item price and title print

item_titles = driver.find_element_by_class_name('c16H9d')
item_prices = driver.find_element_by_class_name('c13VH6')

print(item_titles.text)
print(item_prices.text)

'''


##- Item title is in class ='c16H9d'
##- Item price is in class ='c13VH6'


title_list = []
price_list = []

# #find all element in the first page
item_titles = driver.find_elements_by_class_name('c16H9d')
item_prices = driver.find_elements_by_class_name('c13VH6')

# #print the list 
for item in item_titles:
	title_list.append(item.text)
for item in item_prices:
	price_list.append(item.text)

# print(title_list)
# print(price_list)
# print(len(title_list))
# print(len(price_list))

'''
## - explicit waits
try:
    element1= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "c16H9d"))
    )
    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "c13VH6"))
    )
except:
    driver.quit()

print(f"{element1.text},{element2.text}")
'''


##- next page click button is class=" ant-pagination-next"

try:
    driver.find_element_by_xpath('//*[@class=”ant-pagination-next” and not(@aria-disabled)]').click()
except NoSuchElementException: 
    driver.quit()


dfL = pd.DataFrame(zip(title_list, price_list), columns=['ItemName', 'Price'])
print(dfL)

dfL.to_csv('LazadaData.csv',index=False)

time.sleep(5)
driver.quit()









