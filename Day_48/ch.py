from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
events_html = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_date = [event.text for event in events_html]
print(events_date)
event_title = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_data = [data.text for data in event_title]
print(event_data)
event_dict = {}



driver.quit()