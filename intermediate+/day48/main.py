################################
# Challenge - Cookie Clicker
################################

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value="bigCookie")

def click_button(duration):
    round_time = time.time()
    while time.time() - round_time < duration:
        cookie.click()
        time.sleep(0.01)
    
    upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    if upgrades:
        upgrades[-1].click()
        print("Purchased an upgrade!")

rounds = 0
while rounds <= 20:
    button = click_button(20)
    rounds -= 1
    print(f"Round {rounds}/20 completed!")
