from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time


# function to call every 10 seconds
def my_function():
    while not stop_event.is_set():
        money_value = int(driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))
        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        upgrades.pop()
        upgrade_costs = []
        for upgrade in upgrades:
            upgrade_text = upgrade.text
            upgrade_cost = int(upgrade_text.split("-")[1].strip().replace(",", ""))
            upgrade_costs.append(upgrade_cost)

        affordable_upgrades = [driver.find_element(By.CSS_SELECTOR, value=f"#{upgrades_ids[index]}") for index, cost in
                               enumerate(upgrade_costs) if money_value >= cost]
        try:
            affordable_upgrades[-1].click()
        except IndexError:
            continue
        time.sleep(10)


# Function for your iterative task
def iterative_task():
    while not stop_event.is_set():
        cookie.click()
        # time.sleep(0.001)  # sleep for 0.001 second between iterations to not overwhelm the cpu


# function to stop the program after 5 minutes
def stop_program():
    print("Stopping the program...")
    stop_event.set()  # set the stop event to terminate the threads
    function_thread.join()  # wait for the function-calling thread to finish
    print("Program stopped.")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

# get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
upgrades_ids = [item.get_attribute("id") for item in items]
upgrades_ids.pop()

stop_event = threading.Event()
function_thread = threading.Thread(target=my_function)
function_thread.daemon = True  # daemonize the thread (allows program to exit when main thread exits)
function_thread.start()

# start iterative task in the main thread
iterative_task()

# schedule the stop_program function to run after 5 minutes
timer_thread = threading.Timer(300, stop_program)
timer_thread.start()
cookie_per_sec = driver.find_element(By.CSS_SELECTOR, value="#cps").text
print(cookie_per_sec)
driver.quit()

# TODO: The program works but is not stopping after 5 minutes and neither captures the cps value
