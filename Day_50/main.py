from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

FACEBOOK_USERNAME = "YOUR FACEBOOK USER NAME"
FACEBOOK_PASSWORD = "YOUR FACEBOOK PASSWORD"

chrome_driver_path= "/home/robinson/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com")
time.sleep(2)
login_page = driver(By.XPATH, '//*[@id="q798806120"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]')
login_page.click()

time.sleep(2)
fb_login = driver(By.XPATH,  '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()