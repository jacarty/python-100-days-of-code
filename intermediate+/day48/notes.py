"""
Selenium Webdriver and Game Playing Bot

https://selenium-python.readthedocs.io/

"""

##############################
# Example 1 - Amazon 
##############################

GU_BARS_URL = "https://www.amazon.co.uk/GU-Chocolate-Outrage-Flavour-Energy/dp/B000CSCRHY"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(GU_BARS_URL)
pound_price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
pence_price = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"£{pound_price}.{pence_price}")

# closes the active tab
# driver.close()
# closes the entire browser
driver.quit()

##############################
# Example 2 - Python.org
##############################

URL = "https://www.python.org"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# forms typically use name 
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# find by ID
button = driver.find_element(By.ID, value="submit")
print(search_bar.size)

# find by CSS Selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# find by XPATH
jobs_link = driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[1]/div[4]/p[2]/a')
print(jobs_link.text)

# closes the active tab
# driver.close()
# closes the entire browser
driver.quit()

##############################
# Example 3 - Python.org
##############################

URL = "https://www.python.org"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find by CSS Selector
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# dictionary comprehension with index as key, from the two lists 
events = {n: {time.text: name.text} for n, (time, name) in enumerate(zip(event_times, event_names))}
print(events)

# closes the entire browser
driver.quit()

##############################
# Example 4 - Wikipedia
##############################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find total articles by CSS Selector
article_count = driver.find_elements(By.CSS_SELECTOR, "a[href='/wiki/Special:Statistics']")
print(article_count[1].text)

article_count.click()

# closes the entire browser
driver.quit()

################################
# Example 5 - Click By Link Text
################################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

teahouse = driver.find_element(By.LINK_TEXT, value="Teahouse")
teahouse.click()

# closes the entire browser
driver.quit()

################################
# Example 6 - Input Box Example
################################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find search box
search = driver.find_element(By.NAME, value="search")
# enter text and retrun
search.send_keys("Python", Keys.ENTER)

# closes the entire browser
driver.quit()

################################
# Example 7 - Webpage Sign Up
################################

URL = "https://secure-retreat-92358.herokuapp.com/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

fname.send_keys("Rydon")
lname.send_keys("Man")
email.send_keys("rydonman@mailinator.com")

# instructor
# button = driver.find_element(By.CSS_SELECTOR, value="form button")
button = driver.find_element(By.CSS_SELECTOR, value="button.btn.btn-lg.btn-primary.btn-block")
button.click()

# closes the entire browser
driver.quit()

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
