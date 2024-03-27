from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
import time

load_dotenv()
FACE_USERNAME = os.getenv("FACE_USERNAME")
FACE_PASSWORD = os.getenv("FACE_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://bumble.com/app")
time.sleep(2)

# we must save the current window
main_window = driver.current_window_handle

# login with facebook button
facebook_button = driver.find_element(By.CLASS_NAME, value="color-provider-facebook")
facebook_button.click()
time.sleep(2)

# after clicking loging in the step before a new window appears. We must list the available windows and switch to the
# new one
login_window = None
for handle in driver.window_handles:
    if handle != main_window:
        login_window = handle

driver.switch_to.window(login_window)

# login
email_field = driver.find_element(By.ID, value="email")
email_field.send_keys(FACE_USERNAME)
password_field = driver.find_element(By.ID, value="pass")
password_field.send_keys(FACE_PASSWORD)
login_button = driver.find_element(By.NAME, value="login")
login_button.click()
time.sleep(6)

# change control to main_window again
driver.switch_to.window(main_window)
print(driver.title)  # debug only, to check the window we are in

# give like
for n in range(25):  # bumble limits to 25 likes per day
    time.sleep(3)
    try:
        like_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span')
        like_button.click()
    except ElementClickInterceptedException:
        x_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
        x_button.click()
    else:
        try:
            new_like_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
            new_like_button.click()
        except ElementClickInterceptedException:
            x_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
            x_button.click()

driver.quit()
