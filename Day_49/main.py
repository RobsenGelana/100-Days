from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

ACCOUNT_EMAIL = "YOUR_LOGIN_EMAIL"
ACCOUNT_PASSWORD = "YOUR_LOGIN_PASSWORD"

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in_button = driver(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver(By.ID, "#username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver(By.ID, "#password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)