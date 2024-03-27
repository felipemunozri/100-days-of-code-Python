from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# To keep Chrome browser open after program finishes first we must create an instance of ChromeOptions() and store it in
# a variable. From that variable we call the add_experimental_option() method and for the value 'detach' we set it to
# True.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# then we create an instance of the selenium Chrome webdriver and pass the chrome_options instance.
driver = webdriver.Chrome(options=chrome_options)

# to open the browser we can use the .get() method passing a website url
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# to scrap information from a website we can use the find_element() function together with the By functionality (we must
# import it first). We can use By to select elements by name, class, id, css selectors, xpath, etc.
product_price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
product_price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
product_price = float(f"{product_price_whole}.{product_price_cents}")
print(product_price)

# when we use the find_element() function selenium doesn't return a html element, instead it returns a selenium element,
# and from it, we can tap into several properties
searchbar = driver.find_element(By.NAME, value="field-keywords")
print(searchbar.get_attribute(name="placeholder"))

search_button = driver.find_element(By.ID, value="nav-search-submit-button")
print(search_button.size)

send_to_link = driver.find_element(By.CSS_SELECTOR, value=".a-declarative a")
print(send_to_link.text)

signup_link = driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[1]/div/div[3]/ul/li[1]/a')
print(signup_link.text)

# to close the browser programmatically we can use the methods close() or quit(). The difference between close() and
# quit() is that close() closes the current browser tab that our program opened, while quit() closes the entire
# browser window the program opened. The latter is useful when our program has opened several tabs
# driver.close()
driver.quit()

