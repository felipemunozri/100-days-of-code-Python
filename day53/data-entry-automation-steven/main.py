from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Soup:
    
    def __init__(self, url):
        self.listing_price = []
        self.listing_address = []
        self.listing_link = []
        self.list_len = None
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.get(url)
        
        self.soup = self.create_soup()
        self.scrape()
    
    def create_soup(self):
        time.sleep(4)                
        
        for _ in range(20):
            webdriver.ActionChains(driver=self.driver).key_down(Keys.TAB).perform()
        for _ in range(140):
            webdriver.ActionChains(driver=self.driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        
        zillow = self.driver.page_source
        return BeautifulSoup(zillow, "html.parser")
        
    def scrape(self):
        property_list = self.soup.select(selector="ul li .property-card-data")
        for i in range(len(property_list)):
            address = property_list[i].select_one("address[data-test=property-card-addr]").getText()
            price = property_list[i].select_one("span[data-test=property-card-price]").getText().split(" ")[0].strip("+")
            link = property_list[i].select_one(".property-card-link").get("href")
            
            if "/" in price:
                price = price.split("/")[0].strip("+")
            
            if not link.startswith("http"):
                link = "https://www.zillow.com" + link
            
            self.listing_address.append(address)
            self.listing_price.append(price)
            self.listing_link.append(link)


ZILLOW_SEARCH_URL = ("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481631640625%2C%22east%22%3A-122.22184268359375%2C%22south%22%3A37.644920172866975%2C%22north%22%3A37.905434239337794%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A553006%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D")

soup = Soup(ZILLOW_SEARCH_URL)
print(soup.listing_address)
print(soup.listing_price)
print(soup.listing_link)
