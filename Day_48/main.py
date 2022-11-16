from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/Dell-XPS-9310-Laptop-Touchscreen/dp/B0BB1HF9WY/ref=sr_1_4?keywords=dell+xps+13&qid=1668607207&sprefix=dell%2Caps%2C569&sr=8-4")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)
driver.quit()