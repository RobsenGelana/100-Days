from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

ou = [event.text for event in events]
print(ou)

driver.quit()