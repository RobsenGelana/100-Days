from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/JBL-VIBE-100-TWS-Ear/dp/B095J56XV5/ref=sr_1_3?crid=VSPD71L344NY&keywords=wireless+earbuds&qid=1668606840&sprefix=wire%2Caps%2C465&sr=8-3")
price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print(price.text)
driver.quit()