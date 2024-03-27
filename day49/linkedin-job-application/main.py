from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
LINKEDIN_URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3705674634&geoId=104621616&keywords=junior%20python"
                "%20developer&location=Chile&origin=JOBS_HOME_LOCATION_SUGGESTION&refresh=true&start=25")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(LINKEDIN_URL)
time.sleep(2)

# click login button
login_button = driver.find_element(By.XPATH, '/html/body/div[4]/a[1]')
login_button.click()

# fill login form
username_field = driver.find_element(By.ID, value="username")
username_field.send_keys(LINKEDIN_USERNAME, Keys.TAB)
password_field = driver.find_element(By.ID, value="password")
password_field.send_keys(LINKEDIN_PASSWORD, Keys.RETURN)

# click
minimize_chat_button = driver.find_element(By.XPATH, value='//*[@id="ember41"]')
minimize_chat_button.click()

# click save-job button
# save_job_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
# save_job_button.click()
