from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
price = driver.find_element(By.NAME, "q")
print(price.get_attribute("placeholder"))
driver.quit()