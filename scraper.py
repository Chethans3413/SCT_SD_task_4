# ---------------------------------------------------------
# Program: E-commerce Web Scraper
# Task: 04 - SkillCraft Technology
# Author: Chethan S.
# Description: Extracts book names, prices, and ratings 
#              from a website and saves them to a CSV.
# ---------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    url = "http://books.toscrape.com/"
    
    # 1. Send a request to the website
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return

    # 2. Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    data = []

    # 3. Extract specific information
    for book in books:
        # Get Name
        title = book.h3.a["title"]
        
        # Get Price
        price = book.find("p", class_="price_color").text
        
        # Get Rating (contained in the class name, e.g., "star-rating Three")
        rating_classes = book.find("p", class_="star-rating")["class"]
        rating = rating_classes[1]  # The second class name is the rating word
        
        # Get Availability
        availability = book.find("p", class_="instock availability").text.strip()

        # Add to our list
        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    # 4. Save data to a CSV file using Pandas
    df = pd.DataFrame(data)
    df.to_csv("products.csv", index=False)
    
    print("--- Success! ---")
    print(f"Extracted {len(data)} products.")
    print("Data saved to 'products.csv'")

if __name__ == "__main__":
    scrape_books()
