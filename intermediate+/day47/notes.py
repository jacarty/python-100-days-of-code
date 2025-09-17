"""
Amazon Price Tracker

Check Price. Compare to Target. Email if cheaper.

Camel Camel Camel
https://uk.camelcamelcamel.com/product/B000CSCRHY 
average price over 12 months = £28.67 
live price today on Amazon = £51.60
"""

import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from dotenv import load_dotenv
import os
from notification_manager import NotificationManager

load_dotenv("../../.env")

GU_BARS_URL = "https://www.amazon.co.uk/GU-Chocolate-Outrage-Flavour-Energy/dp/B000CSCRHY"
HEADERS = {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
TARGET_PRICE = Decimal('28.67')

def fetch_amazon_page(gu_bars_url, headers):
    """Fetch the Amazon Product Page"""

    response = requests.get(gu_bars_url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_price(website_html):
    """Soup Price Extraction"""

    soup = BeautifulSoup(website_html, 'html.parser')

    try:
        gu_price_whole = soup.find("span", class_="a-price-whole").get_text()
        gu_price_fraction = soup.find("span", class_="a-price-fraction").get_text()
    except AttributeError:
        return "Could not find price on page. Amazon may have changed their HTML structure."

    gu_price = Decimal(f"{gu_price_whole}{gu_price_fraction}")
    return gu_price

def check_and_notify(current_price, target_price, gu_bars_url):
    """Price Check and Email"""

    notifications = NotificationManager()

    if current_price < target_price:
        recipient = os.getenv("RECIPIENT")
        subject = "Amazon Price Alert - Gu Buy Time!"
        message = f"Guud news. The price has dropped to {current_price}. Time to stock up.\n{gu_bars_url}"
        send_email = notifications.send_email(recipient, subject, message)
        return send_email
    else:
        return "No Gu Buy"

def main():
    try:
        website_html = fetch_amazon_page(GU_BARS_URL, HEADERS)
        current_price = extract_price(website_html)
        outcome = check_and_notify(current_price, TARGET_PRICE, GU_BARS_URL)
        print(outcome)
    except (requests.RequestException, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()