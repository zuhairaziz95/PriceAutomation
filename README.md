#### PriceAutomation

- Creating automation to extract price and item title from ecommerce website which is Lazada.com.my. 
The module that I used is Selenium. ('EcomScraper.py')
The step is straightforward which is using bot automation inside ChromeDriver that will help navigate thru the website we want, search and etc.
Find the element class or id for the title and prices and finally append it into a csv dataframe.

  - Succesfully extract the data from Lazada and enter any item you wanted and it will extract all the data you wanted.
  From the data, the first page is the most relate to the search query, the other pages only return uncessary data.

- The 2nd method I tried was using BeautifulSoup ('ScraperBS_Test.py'). However the Amazon that I was trying to access is very sensitive,
We have to special access to scrape the data we want. So to no avail!

