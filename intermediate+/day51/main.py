"""
Twitter Complaints Bot
"""

from dotenv import load_dotenv
import os
import tempfile
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Constants
load_dotenv("../../.env")
SPEEDTEST_URL = "https://www.speedtest.net/"
SLA_DOWN = 500
SLA_UP = 10
TWITTER_URL = "https://twitter.com"
TWITTER_U = os.getenv("TWITTER_U")
TWITTER_PW = os.getenv("TWITTER_PW")

class InternetSpeedTwitterBot:

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
        self.test_wait = WebDriverWait(self.driver, timeout=60)
        self.standard_wait = WebDriverWait(self.driver, timeout=5)

        # Properties
        self.up = 0
        self.down = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.driver.quit()
        pass

    def get_internet_speed(self):    
        try:
            self.driver.get(SPEEDTEST_URL)
            test_button = self.standard_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "start-button")))
            test_button.click()

            try:
                close_popup = self.test_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-btn")))
                close_popup.click()
                print("Closed popup")
            except:
                print("No popup appeared")

            download = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-download-status-value].result-data-large")))
            upload = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-upload-status-value].result-data-large")))

            self.down = float(download.text)
            self.up = float(upload.text)

            print(f"Download: {self.down} Mbps")
            print(f"Upload: {self.up} Mbps")
            print(f"SLA - Down: {SLA_DOWN} Mbps, Up: {SLA_UP} Mbps")

            if self.down < SLA_DOWN or self.up < SLA_UP:
                print("⚠️  Speed below SLA! Time to tweet at provider!")
                return True
            else:
                print("✅ Speed meets SLA requirements")
                return False
   
        except Exception as e:
            return f"Start unsuccessful: {e}"

    def tweet_at_provider(self):
        try:
            self.driver.get(TWITTER_URL)
            print("Navigated to Twitter")
            
            login_button = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="loginButton"]')))
            login_button.click()
            print("Login button clicked")

            # Wait for the login modal to appear (no iframe needed)
            login_modal = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[role="dialog"]')))
            print("Login modal appeared")

            input_area = self.standard_wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Phone, email address, or username']")))
            self.driver.execute_script("arguments[0].click();", input_area)
            print("Clicked on input area using JavaScript")
            
            # Wait a moment for the input field to be created
            time.sleep(1)

            username = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
            username.send_keys(TWITTER_U)
            print("Username entered")
            
            time.sleep(1.2)

            next_button = self.standard_wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]')))
            next_button.click()
            print("Next button clicked")

            time.sleep(0.8)

            password = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="current-password"]')))
            password.send_keys(TWITTER_PW)  # Fixed: use password, not username
            print("Password entered")

            time.sleep(1.5)

            final_login_button = self.standard_wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]')))
            final_login_button.click()
            print("Final login button clicked")

            # Wait a bit for login to complete
            print("Waiting for login to complete...")
            
            time.sleep(1.2)
            
            tweet_box = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
            tweet_box.send_keys(f"Hey Internet Provider. Why is my internet {self.down}down/{self.up}up when I pay for {SLA_DOWN}down and {SLA_UP}up?")
            print("Tweet text entered")

            time.sleep(5)

            tweet_button = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')))
            tweet_button.click()
            print("Tweet posted!")

            return "Tweet sent successfully"
            
        except Exception as e:
            print(f"Twitter automation failed at step: {e}")
            return f"Failed to tweet: {e}"

if __name__ == "__main__":
    with InternetSpeedTwitterBot() as app:
        should_tweet = app.get_internet_speed()
        
        if should_tweet is True:
            tweet_result = app.tweet_at_provider()
            print(f"Tweet result: {tweet_result}")

        elif should_tweet is False:
            print("No need to complain - speeds are good!")
            
        else:
            print(f"Error: {should_tweet}")
