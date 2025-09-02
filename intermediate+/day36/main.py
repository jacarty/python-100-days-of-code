from dotenv import load_dotenv
import os
import requests

load_dotenv("../../.env")

ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API = os.getenv("NEWS_API")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_API_KEY
}

data = requests.get(url=ALPHA_URL, params=alpha_parameters)
data.raise_for_status()
tsla_stock_data = data.json()["Time Series (Daily)"]
# print(tsla_stock_data)

closing_prices = {
    date: float(data["4. close"]) 
    for date, data in tsla_stock_data.items()
}

values = list(closing_prices.values())
close = values[0]   # 333.87
previous_close = values[1]  # 345.98
percentage_change = ((close - previous_close) / previous_close) * 100

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs(percentage_change) > 5:
    print(f"Get News - Stock moved {percentage_change:+.1f}%")

    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API
    }

    news = requests.get(url=NEWS_URL, params=news_parameters)
    news.raise_for_status()
    news_articles = news.json()["articles"][:3]
    print(news_articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

