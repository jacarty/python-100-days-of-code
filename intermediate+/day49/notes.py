"""
Selenium to book fake gym classes

"""

import os
import tempfile
import textwrap
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOGIN_URL = "https://appbrewery.github.io/gym/"
SCHEDULE_URL = "https://appbrewery.github.io/gym/schedule/"
ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""

days = ["tue", "thu"]
timeslot = "1800"
already_on = 0 
waitlist = 0
booked = 0
classes = []

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

def find_day_container(driver, day):
    selectors = [
        f"div[id*='day-group-today-({day},']",      # Today pattern
        f"div[id*='day-group-tomorrow-({day},']",   # Tomorrow pattern  
        f"div[id*='day-group-{day}']"               # Regular day pattern
    ]
    for selector in selectors:
        try:
            return driver.find_element(By.CSS_SELECTOR, selector)
        except:
            continue

    raise Exception(f"Could not find container for day: {day}")

def book_class(container, day, time):
    
    global already_on
    global waitlist
    global booked
    global classes

    try:
        # find card for time (e.g. 1800)
        gym_class = container.find_element(By.CSS_SELECTOR, f"div[id^='class-card-'][id*='{time}']")
        # find the date (of class)
        gym_class_date = container.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs")
        # find the class type
        gym_class_type = container.find_element(By.CSS_SELECTOR, "h3[id^='class-name']")
        # find the button
        gym_class_button = gym_class.find_element(By.CSS_SELECTOR, "button")

        # Check if a class is already booked (button reads "Booked")
        if gym_class_button.text == "Booked":
            classes.append(f"Booked: {gym_class_type.text} on {gym_class_date.text} at {time}")
            already_on += 1

        # Check if you're on the waitlist (button reads "Waitlisted")
        elif gym_class_button.text == "Waitlisted":
            classes.append(f"Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            already_on += 1

        # Join the waitlist if the class is full (button says "Join Waitlist")
        elif gym_class_button.text == "Join Waitlist":
            gym_class_button.click()
            # print(f"✓ Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            waitlist +=1
            classes.append(f"Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")

        else:
            gym_class_button.click()
            # print(f"✓ Booked: {gym_class_type.text} on {gym_class_date.text} at {time}")
            booked += 1
            classes.append(f"New booking: {gym_class_type.text} on {gym_class_date.text} at {time}")

    except Exception as e:
        print(f"Booking unsuccessful: {e}")
        return False

def verify_bookings(driver):
    my_bookings = driver.find_element(By.ID, "my-bookings-link")
    my_bookings.click()

    wait = WebDriverWait(driver, timeout=10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MyBookings_bookingCard__VRdrR")))

    try:
        booked_classes = driver.find_elements(By.CLASS_NAME, "MyBookings_bookingCard__VRdrR")
        print(booked_classes)
        booked_total = len(booked_classes)

        return booked_total
    
    except NoSuchElementException:
        return 0

def counters(total_booked):

    total_classes = booked + waitlist + already_on

    if total_classes == total_booked:
        result = "✅ SUCCESS: All bookings verified!"
    else:
        result = "❌ MISSING: Booking mismatch!"

    return f"""
    --- BOOKING SUMMARY ---
    Classes booked: {booked}
    Waitlists joined: {waitlist}
    Already booked/waitlisted: {already_on}
    Total 6pm classes processed: {total_classes}
        
    --- DETAILED CLASS LIST ---
    {'\n    '.join(classes)}
    
    --- VERIFICATION RESULT ---
    Found: {total_booked} bookings
    {result}
    """

def main(driver, url, email, password, days, timeslot):
    # login
    login(driver, url, email, password)

    # book classes
    for day in days:
        container = find_day_container(driver, day)
        booking = book_class(container, day, timeslot)
        print(booking)
    
    # verify what is booked
    total_booked = verify_bookings(driver)

    # return counters
    summary = counters(total_booked)
    print(summary)
    
    #driver.quit()

if __name__ == "__main__":
    main(driver, 
         LOGIN_URL, 
         ACCOUNT_EMAIL, 
         ACCOUNT_PASSWORD,
         days,
         timeslot)
