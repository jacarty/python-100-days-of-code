"""
Let's Find Thai Cuisine Recipes - my favourite!
https://www.allrecipes.com/
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

cuisine = 'thai'

def navigate(cuisine):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    driver = None
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        print("Chrome driver started successfully")
        
        print("Navigating directly to Cuisines A-Z page...")
        driver.get("https://www.allrecipes.com/cuisine-a-z-6740455")
        
        wait = WebDriverWait(driver, 20)
        
        print("Checking for cookie consent popup...")
        try:
            reject_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reject All')]"))
            )
            print("Cookie popup found - clicking 'Reject All'")
            reject_button.click()
            time.sleep(2)
            print("Cookie popup dismissed")
        except TimeoutException:
            print("No cookie popup found or already dismissed")

        print("Waiting for page to fully load...")
        time.sleep(3)
        
        print(f"Searching for {cuisine.title()} cuisine...")
        cuisine_links = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.mntl-link-list__link"))
        )
        
        print(f"Found {len(cuisine_links)} cuisine links")
        
        cuisine_found = False
        for link in cuisine_links:
            if cuisine.lower() in link.text.lower():
                print(f"Found '{link.text}'! Clicking...")
                driver.execute_script("arguments[0].click();", link)
                cuisine_found = True
                break
        
        if not cuisine_found:
            print(f"Could not find {cuisine} in the list!")
            available_cuisines = [link.text.strip() for link in cuisine_links[:15]]
            print(f"Available cuisines: {available_cuisines}")
            return None

        print("Waiting for cuisine page to load...")
        time.sleep(5)

        print("Getting page source...")
        page_source = driver.page_source
        
        print("Successfully retrieved page!")
        return page_source
        
    except Exception as e:
        print(f"Error during navigation: {e}")
        import traceback
        traceback.print_exc()
        return None
    finally:
        if driver:
            driver.quit()
            print("Browser closed")


def get_recipes(cuisine):
    print(f"Starting recipe scraper for {cuisine.title()} cuisine...")
    response = navigate(cuisine)
    
    if not response:
        print("Failed to get page content")
        return
    
    soup = BeautifulSoup(response, 'html.parser')
    
    recipes = []

    recipe_cards = soup.find_all('a', class_='mntl-card-list-items')
    
    print(f"Found {len(recipe_cards)} recipes!")

    for card in recipe_cards:
        recipe_url = card.get('href')

        card_content = card.find('div', class_='card__content')
        data_tag = card_content.get('data-tag') if card_content else None
        
        title_span = card.find('span', class_='card__title-text')
        title = title_span.get_text(strip=True) if title_span else None
        
        recipes.append({
            'category': data_tag,
            'title': title,
            'url': recipe_url
        })

    filename = f'{cuisine}_recipes.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        for recipe in recipes:
            f.write(f"Category: {recipe['category']}\n")
            f.write(f"Title: {recipe['title']}\n")
            f.write(f"URL: {recipe['url']}\n")
            f.write("-" * 50 + "\n\n")
    
    print(f"✓ Successfully saved {len(recipes)} recipes to {filename}")

if __name__ == "__main__":
    get_recipes(cuisine)
