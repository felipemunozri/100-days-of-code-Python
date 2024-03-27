import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import lxml
import requests

# Zillow search result url for properties for rent in the area of San Francisco CA, with a price under 3K and at least
# 1 bedroom
ZILLOW_SEARCH_URL = ("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481631640625%2C%22east%22%3A-122.22184268359375%2C%22south%22%3A37.644920172866975%2C%22north%22%3A37.905434239337794%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A553006%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D")

# url of the Google Form to be filled using selenium
GOOGLE_FORM_URL = "https://forms.gle/2xUrHtVzy61Jh4Tb8"


# TODO : 1. use BS to scrap the price, address and url of the search results from the ZILLOW_URL

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
}
response = requests.get(ZILLOW_SEARCH_URL, headers=headers)
response.raise_for_status()
data = response.text
soup = BeautifulSoup(data, "lxml")

# get the prices
price_elements = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
prices_list = [price.text[1:6].replace(",", "") for price in price_elements]

# get the addresses
address_elements = soup.select(selector="a address")
addresses_list = [address.text for address in address_elements]

# get the links
link_elements = soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0")
# some links are relative url, so we must check and convert them to absolute urls
links_list = []
for link in link_elements:
    link_url = link.get(key="href")
    site_url = "https://www.zillow.com"
    if site_url in link_url:
        links_list.append(link_url)
    else:
        links_list.append(site_url + link_url)

# print(prices_list)
# print(addresses_list)
# print(links_list)

# TODO: 2. use selenium to fill a google form for each scrapped piece of data (form is created previously).

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("window-size=1366,768")
driver = webdriver.Chrome(options=chrome_options)

driver.get(url=GOOGLE_FORM_URL)
input_elements = driver.find_elements(By.CSS_SELECTOR, value=".Xb9hP input")
address_input = input_elements[0]
price_input = input_elements[1]
link_input = input_elements[2]

for i in range(len(addresses_list)):
    time.sleep(2)
    input_elements = driver.find_elements(By.CSS_SELECTOR, value=".Xb9hP input")
    address_input = input_elements[0]
    price_input = input_elements[1]
    link_input = input_elements[2]

    address_input.send_keys(addresses_list[i])
    price_input.send_keys(prices_list[i])
    link_input.send_keys(links_list[i])
    link_input.send_keys(Keys.TAB, Keys.RETURN)
    time.sleep(2)
    try:
        new_answer_link = driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a")
        new_answer_link.click()
    except NoSuchElementException:
        continue

driver.quit()
