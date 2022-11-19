from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


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

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver(By.XPATH, '//*[@id="email"]')
password = driver(By.XPATH, '//*[@id="pass"]')
email.send_keys(FACEBOOK_USERNAME)
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
time.sleep(5)

#Allow location
allow_location_button = driver(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()