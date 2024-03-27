from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3705674634&geoId=104621616&keywords=junior%20python"
           "%20developer&location=Chile&origin=JOBS_HOME_LOCATION_SUGGESTION&refresh=true&start=25")

# Click Reject Cookies Button
# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(LINKEDIN_USERNAME)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(LINKEDIN_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
# input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
# all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value="jobs-search-results__list-item")


# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
