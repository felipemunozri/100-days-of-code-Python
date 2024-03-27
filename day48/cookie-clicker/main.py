from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# get the cookie element to click
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

# get the upgrade items ids
upgrade_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
upgrade_items_ids = [item.get_attribute("id") for item in upgrade_items]
upgrade_items_ids.pop()  # remove the last item because it's empty

timeout = time.time() + 5  # set a time interval of 5 seconds from the current time
five_min = time.time() + 60 * 5  # set a time interval of 5 minutes from the current time

while True:
    cookie.click()
    # every 5 seconds we check for our money count and possible upgrades to buy
    if time.time() > timeout:
        # get ahold of the text value, remove ',' and convert to int
        money_count = int(driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))

        # get upgrade elements
        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        upgrades.pop()

        # for every upgrade in upgrades we get the upgrade price and append it to a list
        upgrade_prices = []
        for upgrade in upgrades:
            upgrade_text = upgrade.text
            upgrade_price = int(upgrade_text.split("-")[1].strip().replace(",", ""))
            upgrade_prices.append(upgrade_price)

        # now we compare our current money count value against each upgrade price in the upgrade_prices list. If our
        # money is greater or equal than any value, it means we can afford it and hence we use its index to search the
        # element and append it to the affordable_upgrades list
        affordable_upgrades = [driver.find_element(By.CSS_SELECTOR, value=f"#{upgrade_items_ids[index]}")
                               for index, cost in enumerate(upgrade_prices) if money_count >= cost]
        # from this list we will get the last value (the most expensive one but also the most useful to produce more
        # cookies) and we click on it to purchase it
        affordable_upgrades[-1].click()

        # after we buy an upgrade we add another 10 seconds to our timeout to be able to regain some money and be able
        # to buy a new upgrade
        timeout = time.time() + 10

    # after 5 minutes we stop our program, and we check the cookies per second (cps) count that we achieved
    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.CSS_SELECTOR, value="#cps").text
        print(cookie_per_sec)
        break

driver.quit()
