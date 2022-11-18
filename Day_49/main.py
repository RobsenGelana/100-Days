from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 

ACCOUNT_EMAIL = "YOUR_LOGIN_EMAIL"
PHONE = "ENTER YOUR PHONE NUMBER"
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

time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()