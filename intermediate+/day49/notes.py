"""
Selenium to book fake gym classes

"""

import os
import tempfile
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOGIN_URL = "https://appbrewery.github.io/gym/"
SCHEDULE_URL = "https://appbrewery.github.io/gym/schedule/"
ACCOUNT_EMAIL = "rydonman@mailinator.com"
ACCOUNT_PASSWORD = "Password123"

# Chrome profile data
user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")

# Chrome setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)

def login(driver, url, email, password):
    driver.get(url)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    wait = WebDriverWait(driver, timeout=10)

    try:
        email_field = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "password-input")))
        password_field.clear()
        password_field.send_keys(password)

        submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-button")))
        submit_button.click()

        wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

        return True
    
    except Exception as e:
        print(f"Login unsuccessful: {e}")
        return False

def book_class(driver, day, time):

    try:
        container = driver.find_element(By.CSS_SELECTOR, f"div[id^='day-group-{day}']")
        gym_class = container.find_element(By.CSS_SELECTOR, f"div[id^='class-card-'][id*='{time}']")
        gym_class_date = container.find_element(By.CSS_SELECTOR, f"h2[id^='day-title-{day}']")
        gym_class_type = container.find_element(By.CSS_SELECTOR, "h3[id^='class-name']")
        gym_class_time = gym_class.find_element(By.CSS_SELECTOR, "p[id^='class-time']")
        gym_class_button = gym_class.find_element(By.CSS_SELECTOR, "button")
        gym_class_button.click()

        print(f"✓ Booked: {gym_class_type.text} on {gym_class_date.text} at {gym_class_time.text}")        
        return True
    
    except Exception as e:
        print(f"Booking unsuccessful: {e}")
        return False
        
def main():    
    login(driver, LOGIN_URL, ACCOUNT_EMAIL, ACCOUNT_PASSWORD)
    book_class(driver, "tue", "1800")

if __name__ == "__main__":
    main()
