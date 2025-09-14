"""
 Web Scraping With Beautiful Soup

 https://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""

# Beautiful Soup
from bs4 import BeautifulSoup
# import lxml

with open("./index.html") as file:
    html_content = file.read()
    print(html_content)

# if html doesnt work try lxml
soup = BeautifulSoup(html_content, 'html.parser')

# print title tag
print(soup.title)
# print title name
print(soup.title.name)
# print title text
print(soup.title.string)
# formats the output
print(soup.prettify())

# print first anchor tag it finds
print(soup.a)
# print first list it finds
print(soup.li)
# print first paragraph it finds
print(soup.p)

# find all instances of X
all_paragraphs = soup.find_all("p")
print(all_paragraphs)

# find all instances of X
all_anchor_tags = soup.find_all("a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

# search by tag or heading
heading = soup.find(name="h1", id="heading")

# search by class, note _ at end of class
section_heading = soup.find(name="h3", class_="TV")
print(section_heading)

# search by CSS selector
selector = soup.select_one(selector="#name")

# search by CSS class
headings = soup.select(".heading")


######################################################
# Hackernew 
# Aim is to get the most upvoted article in the top 30
######################################################

from bs4 import BeautifulSoup
import requests

site = "https://news.ycombinator.com/news"
response = requests.get(site)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# return articles from first page
articles = soup.find_all("span", class_="titleline")

# generate two lists
articles_text = [] 
articles_url = []

# add Article Header and URL to lists
for article in articles:

    text = article.get_text()
    articles_text.append(text)

    url = article.find("a").get("href")
    articles_url.append(url)

# list comprehension to get the scores per article
article_upvotes = [int(votes.get_text().split()[0]) for votes in soup.find_all("span", class_="score")]

# print(articles_text)
# print(articles_url)
# print(article_upvotes)

# return index of highest score
max_score_index = article_upvotes.index(max(article_upvotes))

# print the list items corresponding to score
print(f"This article with the most votes is: {articles_text[max_score_index]} -> {articles_url[max_score_index]}")

######################################################
# Webscraping
# 
# Legal Rules for Web Scraping (via Claude)
#
# 1. Check the robots.txt File
# Before scraping any website, always check website.com/robots.txt. This file tells you:
# Which parts of the site you can scrape
# Which parts are off-limits
# Crawl delay requirements
# Example:
# Always check: https://example.com/robots.txt
# # It might contain:
#   User-agent: *
#   Disallow: /private/
#   Crawl-delay: 1
#
# 2. Review the Terms of Service (ToS)
# Many websites explicitly prohibit scraping in their Terms of Service. Violating ToS can lead to:
#   IP bans
#   Legal action
#   Account termination (if logged in)
#
# 3. Respect Rate Limits
#   Add delays between requests (typically 1-3 seconds)
#   Don't overwhelm servers with rapid requests
#   This is both ethical and helps avoid getting blocked
#       pythonimport time
#       time.sleep(2)  # Wait 2 seconds between requests
#
# 4. Copyright and Data Ownership
#   Factual data generally can't be copyrighted
#   Creative content (articles, images) is usually protected
#   Database compilations may have protection
#   Always consider fair use, but it's complex
# 
# Best Practices for Legal Scraping
# 
#   1. Use APIs When Available
#       Many sites offer APIs specifically for data access - always prefer these over scraping.
#   2. Identify Yourself
#       Set a proper User-Agent header:
#       pythonheaders = {
#           'User-Agent': 'Your Bot Name (your-email@example.com)'
#       }
#
#   3. Handle Personal Data Carefully
#
#       GDPR (Europe) and CCPA (California) have strict rules about personal data
#       Avoid scraping personal information when possible
#       If you must, ensure compliance with privacy laws
#
#   4. Respect "No Scraping" Signs
#
#   If you see:
#       Meta tags like <meta name="robots" content="noindex,nofollow">
#       Explicit "no scraping" notices
#       CAPTCHA challenges
#       These are clear signals to stop.
#
# Common Legal Pitfalls to Avoid
#
#   Don't bypass security measures (login walls, CAPTCHAs)
#   Don't scrape copyrighted content for commercial use
#   Don't violate Computer Fraud and Abuse Act (CFAA) - unauthorized access
#   Don't ignore cease and desist letters
#   Don't resell or redistribute scraped data without permission
#
# Gray Areas and Recent Cases
#
#   LinkedIn vs. HiQ Labs (2019): Publicly available data may be fair game
#   Facebook vs. Power Ventures: Logged-in scraping is riskier
# 
#   The legal landscape is evolving - what's okay today might not be tomorrow
######################################################

"""
Challenge

Empire 
Return the Top 100 Movies and output to txt file
"""

from bs4 import BeautifulSoup
import requests

site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(site)
website_html = response.text
# print(response.text)

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())

# list comprehensin for movie names; 100 to 1
movies = [movie.text for movie in soup.find_all("h3", class_="title")]

# reverse list and appeend each to file
with open("./movies.txt", "a") as f:
    for movie in reversed(movies):
        f.write(f"{movie}\n")
