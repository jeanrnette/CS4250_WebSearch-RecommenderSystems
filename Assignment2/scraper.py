#-------------------------------------------------------------------------
# AUTHOR: Jeannette Ruiz
# FILENAME: scraper.py
# SPECIFICATION: Program that crawls Circular Links section of TestingURL.dev
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 1 Hr
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
frontier = [seed]
seen = [seed]


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)


    # Retrieving and parsing the Web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


    # Printing the text contained in the <h1> element
    h1 = soup.find("h1")
    # Check if no <h1> to avoid crash
    if h1 is not None:
        # Req 2: print text contained in <h1> element
        print(h1.get_text())

    # Extracting and processing hyperlinks
    # links: To hold valid links
    links = []

    # Req 3: extract all hyperlinks in <a> tags
    anchors = soup.find_all("a")
    
    for anchor in anchors:
       href = anchor.get("href")

       # If current <a> tag has no href, skip it, go to next <a> tag
       if href is None:
            continue

       # Req4: Converting relative URLs to absolute URLs
       if href.startswith("/"):
            href = baseURL + href

       # Req 5: Following only the hyperlinks that begin with the seed URL
       if href.startswith(seed):
            links.append(href)

    # Sort links (like in pseudocode)
    links.sort()

    # Req 6: Processing each URL once
    for link in links:
        if link not in seen:
            seen.append(link)
            frontier.append(link)


# Req 7: Printing all URLs in seen
for url in seen:
    print(url)