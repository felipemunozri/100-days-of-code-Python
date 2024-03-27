from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

GOOGLE_FORM_LINK = "https://forms.gle/b1i5AXFUw3K8Wkq87"

WEB_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22usersSearchTerm%22%3A%2295815%22%2C%22mapBounds%22%3A%7B%22west%22%3A-121.4121377510402%2C%22east%22%3A-121.12749198641737%2C%22south%22%3A38.598817361099464%2C%22north%22%3A38.88400696186165%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22price%22%3A%7B%22max%22%3A609848%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22customRegionId%22%3A%221220d5fef3X1-CR1iol6gn2xc5mm_12jth5%22%7D"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('window-size=1440,1440')
driver = webdriver.Chrome(options=options)


def get_lease_list():
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, "html.parser")
    return soup.select("ul li article")


def get_all_leases():
    driver.get(WEB_URL)
    time.sleep(4)
    lease_list = []
    # pagination and fetch data.(Up to page 4 for now)
    for page in range(1, 3):
        if page == 1:
            for _ in range(20):
                webdriver.ActionChains(driver).key_down(Keys.TAB).perform()
        for _ in range(120):
            webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
        lease_list.extend(get_lease_list())
        page_list = driver.find_elements(By.CSS_SELECTOR, value=".search-pagination a")[1:-1]
        page_list[page].click()
        time.sleep(2)
    # Convert to dictionary. (For practice)
    lease_dic = {}
    for n in range(len(lease_list)):
        address = lease_list[n].select_one(".list-card-addr").getText()
        price = \
            lease_list[n].select_one(".list-card-price").getText().split("/")[0].split("+")[0].replace("$", "").split(
                " ")[
                0]
        link = lease_list[n].select_one(".list-card-link").get("href")
        # get absolute path
        link = urljoin(WEB_URL, link)
        lease_dic.update({n: {"address": f"{address}", "price": f"{price}", "link": f"{link}"}})
    print(lease_dic)
    return lease_dic


# Fill out the form.
# def input_form(lease_dic):
#     driver.get(GOOGLE_FORM_LINK)
#     for lease in lease_dic.values():
#         address = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
#
#         price = driver.find_element(By.XPATH,
#                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
#                                     )
#         link = driver.find_element(By.XPATH,
#                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
#                                    )
#         submit_button = driver.find_element(By.XPATH,
#                                             value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div'
#                                             )
#
#         address.send_keys(f"{lease['address']}")
#         price.send_keys(f"{lease['price']}")
#         link.send_keys(f"{lease['link']}")
#         submit_button.click()
#         submit_another_response_btn = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.XPATH, '//a[text()="Submit another response"]')))
#         submit_another_response_btn.click()
#
#
zillow_lease = get_all_leases()
# input_form(zillow_lease)

driver.quit()
