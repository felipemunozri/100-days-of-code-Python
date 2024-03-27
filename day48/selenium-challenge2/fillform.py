from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# get ahold of each input field in the form element, pass the relevant information and call the submit() method on the
# last one
f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Felipe")
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("M")
email = driver.find_element(By.NAME, value="email")
email.send_keys("myemail@mail.com")
email.submit()

# # another solution is to get ahold of the first input element inside the form element, pass the relevant information
# and call the TAB key to move through the input elements to finally press the RETURN to key to submit
# form = driver.find_element(By.CLASS_NAME, value="form-signin input")
# form.send_keys("Felipe", Keys.TAB, "M", Keys.TAB, "myemail@mail.com", Keys.RETURN)
