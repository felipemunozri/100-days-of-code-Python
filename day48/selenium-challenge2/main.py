from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # we can click on html element by getting ahold of an element and the calling the click() method on them
# articles_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# articles_count.click()

# contents_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# contents_portals.click()

# # when interacting with form element there are several ways to achieve an interaction in which we enter some text and
# # click a submit button. We can get ahold of the element and then call the send_keys() method to pass a string to any
# # text field. Then, we can call the submit() method (the submit method applies only to form elements). We could also get
# # ahold of the button element an call the click() method over it
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.submit()

# there is another way where we can use the send_keys() method to not only pass a string but to press a specific
# keyboard key like TAB (to change between elements for example) or RETURN to press the enter key. For this, first we
# must import the Keys class from selenium.webdriver.common.keys
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python" + Keys.RETURN)


# driver.quit()
