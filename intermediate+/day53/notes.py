"""
Zillow = San Fran, Rent, 3K Max, 1 Bedroom
Use this - https://appbrewery.github.io/Zillow-Clone/

Beautful Soup to Scrape
Selenium to Enter Form
"""

from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import WebDriverException

# Constants
load_dotenv("../../.env")
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GFORM_URL = os.getenv("D53_GFROM_URL")

def scrape_data(url):
    """Get Zillow Reponse"""
    headers = {
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_info(website_html):
    """Soup List Extraction"""

    soup = BeautifulSoup(website_html, 'html.parser')

    try:
        data = soup.find_all("div", class_="StyledPropertyCardDataWrapper")

        addresses = [item.select_one("address[data-test='property-card-addr']").get_text(strip=True).replace(" |", ",")
                for item in data 
                if item.select_one("address[data-test='property-card-addr']")]

        prices = [item.select_one("span[data-test='property-card-price']").get_text(strip=True)[:6]
                for item in data 
                if item.select_one("span[data-test='property-card-price']")]

        urls = [item.select_one("a[data-test='property-card-link']")['href'] 
                for item in data 
                if item.select_one("a[data-test='property-card-link']")]

        properties = list(zip(addresses, prices, urls))

        return properties
    
    except Exception as e:
        print(f"Could not create dictionary. Error: {e}")
        return False

def fill_google_form_by_question_text(driver, question_text, answer):
    """Fill form field by locating the question text first"""
    try:
        # Find the question span
        question_xpath = f"//span[contains(text(), '{question_text}')]"
        question_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, question_xpath)))
        
        # Find the input container for this question
        container = question_element.find_element(By.XPATH, "./ancestor::div[@jscontroller]")
        
        # Look for textarea or input field
        try:
            input_field = container.find_element(By.TAG_NAME, "textarea")
        except:
            input_field = container.find_element(By.TAG_NAME, "input")
        
        input_field.clear()
        input_field.send_keys(answer)
        return True
        
    except Exception as e:
        print(f"Error filling '{question_text}': {e}")
        return False

def submit_form(url, property_list):
    """Submit form fields and loop"""
    # Chrome
    user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-extensions")
    
    # Selenium
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print("Navigated to Form")

    for address, price, url in property_list:
        # Fill each question by its text
        fill_google_form_by_question_text(driver, "address", address)
        fill_google_form_by_question_text(driver, "price", price)
        fill_google_form_by_question_text(driver, "URL", url)
        
        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label*='Submit']")
        submit_button.click()
        
        time.sleep(1)

        # Wait for success page to load
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Your response has been recorded')]")))
        
        # Click "Submit another response"
        submit_another_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
        submit_another_button.click()
        
        # Wait for form to reload
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        
        print(f"Successfully submitted: {address}")

    # Quit browser
    driver.quit()

if __name__ == "__main__":
    zillow_data = scrape_data(ZILLOW_URL)
    soup_list = extract_info(zillow_data)
    submit_form(GFORM_URL, soup_list)