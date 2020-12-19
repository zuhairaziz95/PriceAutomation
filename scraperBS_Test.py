
import requests #request from website
from bs4 import BeautifulSoup #bs module,webscraping


# ##url website we want
# URL = 'https://www.amazon.com/Nintendo-Console-Resolution-802-11ac-Surround/dp/B07RGFF98S/ref=sr_1_4?crid=1YK7GIW4JAK72&dchild=1&keywords=ninetendo.+switch&qid=1608301074&sprefix=nine%2Caps%2C445&sr=8-4'


# ##google it my user agent
# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


# page = requests.get(URL, headers=headers) 

# #pull out information about the webpage
# soup= BeautifulSoup(page.content,'html.parser')

# #print(soup.prettify())

# title = soup.find(id='productTitle')

# print(title)


URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

webpage = requests.get(URL, headers=HEADERS, proxies=proxies)


soup = BeautifulSoup(webpage.content, "lxml")
print(soup.prettify())
# Outer Tag Object
title = soup.find("span", attrs={"id":'productTitle'})

print(title)
'''
# Inner NavigableString Object
title_value = title.string
# Title as a string value
title_string = title_value.strip()
# Printing types of values for efficient understanding
print(type(title))
print(type(title_value))
print(type(title_string))
print()
 
# Printing Product Title
print("Product Title = ", title_string)
'''