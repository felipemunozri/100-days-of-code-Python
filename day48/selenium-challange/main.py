from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# first we get the 'ul' element (list) in the webpage
events_list = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# then we get all the 'li' elements inside the events_list
event_list_items = events_list.find_elements(By.TAG_NAME, value="li")

# for each 'li' element we get the values for the date and name of the event, each inside the 'time' and 'a' elements
# respectively. Once we get ahold of the values, we create a new dictionary and append it to the events_dic dictionary
events_dic = {}
for index, event in enumerate(event_list_items):
    date = event.find_element(By.TAG_NAME, value="time").text
    event_name = event.find_element(By.TAG_NAME, value="a").text
    events_dic[index] = {
        "time": date.split("T")[0],
        "name": event_name
    }

print(events_dic)

# another solution
menu_list = driver.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")
events_dic2 = {i: {"time": menu_list[i].text.split('\n')[0], "name": menu_list[i].text.split('\n')[1]} for i in
            range(0, len(menu_list))}

print(events_dic2)

driver.quit()
