from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
events_date = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

event_title = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event_dict = {}
for n in range(len(events_date)):
    event_dict[n] = {
        'time': events_date[n].text,
        'name': event_title[n].text
    }
print(event_dict)


driver.quit()