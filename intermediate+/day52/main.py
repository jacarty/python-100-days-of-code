"""
Instagram Bot To Follow Accounts
"""

from dotenv import load_dotenv
import os
import tempfile
import time
from random import randint, uniform
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import WebDriverException

# Constants
load_dotenv("../../.env")
URL = "https://instagram.com"
INSTAGRAM_U = os.getenv("INSTAGRAM_U")
INSTAGRAM_PW = os.getenv("INSTAGRAM_PW")
INSTAGRAM_ACC = ""

class InstaFollower:

    def __init__(self):
        # Chrome
        user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-extensions")
        
        # Selenium
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=10)

        # Insta
        self.followers_list = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.driver.quit()
        pass

    def human_delay(self, action_type="default"):
        delays = {
            "clicking": (0.8, 2.2),
            "default": (0.9, 3.2),
            "typing": (2.5, 8.5)
        }
        min_time, max_time = delays.get(action_type, delays["default"])
        time.sleep(uniform(min_time, max_time))

    def login(self):
        try:
            # Navigate to Page
            self.driver.get(URL)
            print("Navigated to Instagram")
            
            # Username field
            try:
                self.human_delay("clicking")
                uname_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Phone number, username or email address']")))
                uname_field.clear()
                self.human_delay("typing")
                uname_field.send_keys(INSTAGRAM_U)
                print("Entered Username")
            except Exception as e:
                print(f"Failed to find Username field: {e}")
                return False
            
            # Password field
            try:
                pword_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Password']")))
                pword_field.clear()
                self.human_delay("typing")
                pword_field.send_keys(INSTAGRAM_PW)
                print("Entered Password")
            except Exception as e:
                print(f"Failed to find Password field: {e}")
                return False
                
            # Login button
            try:
                self.human_delay("clicking")
                login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and not(@disabled)]")))
                login_button.click()
                print("Clicked Login")
            except Exception as e:
                print(f"Failed to click Login button: {e}")
                return False
            
            # Click "Not now" to Save Password
            try:
                save_login_prompt = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]")))
                save_login_prompt.click()
                print("Dismissed save login prompt")
            except Exception as e:
                print(f"Failed to click Login button: {e}")
                return False

        except WebDriverException as e:
            print(f"WEBDRIVER ERROR: Browser/connection issue - {e}")
            return False
        except Exception as e:
            print(f"UNEXPECTED ERROR: {type(e).__name__} - {e}")
            return False

    def find_followers(self):
        try:
            # Navigate to Page
            self.human_delay("default")
            self.driver.get(f"{URL}/{INSTAGRAM_ACC}")
            print(f"Navigated to {INSTAGRAM_ACC}'s Page")

            # Open Followers
            try:
                followers_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]")))
                self.human_delay("clicking")
                followers_link.click()
                print("Clicked followers link")
            except Exception as e:
                print(f"Failed to find followers link: {e}")
                return False

            # List Followers
            try:
                print("Waiting for followers modal to load...")
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='heading' and contains(text(), 'Followers')]")))
                print("Followers modal loaded")
                
                time.sleep(2)  # Give content time to load
                
                self.followers_list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[.//div[text()='Follow']]")))
                print(f"Found {len(self.followers_list)} users to follow")
            except Exception as e:
                print(f"Failed to create followers list: {e}")
                return False

        except WebDriverException as e:
            print(f"WEBDRIVER ERROR: Browser/connection issue - {e}")
            return False
        except Exception as e:
            print(f"UNEXPECTED ERROR: {type(e).__name__} - {e}")
            return False

    def follow(self):
        max_follows = randint(4, 12)

        # Click each button with delays
        for i, button in enumerate(self.followers_list[:max_follows]):
            try:
                # Scroll to button if needed
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                self.human_delay("clicking")
                button.click()
                print(f"Followed user {i+1}")
                
            except Exception as e:
                print(f"Failed to follow user {i+1}: {e}")

if __name__ == "__main__":
    with InstaFollower() as app:
        login = app.login()
        
        if login: 
            find_followers = app.find_followers()

            if find_followers:
                follow = app.follow()
