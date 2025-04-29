from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button")
login.click()
time.sleep(2)

title_text = driver.find_element(By.CLASS_NAME, "app_logo").text
if title_text == "Swagg Labs": #es gehört Swag Labs eigentlich
    print("Hat funktioniert")
else:
    print("Hat nicht funktioniert")
    driver.save_screenshot("login_faled.png")

driver.quit()
# API-Testing Feature Branch aktiv – Test 1
