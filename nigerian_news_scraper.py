import requests
from bs4 import BeautifulSoup

# This project shows how to collect "Real World" data for AI training.
# We are extracting headlines to build a dataset for Nigerian NLP research.

def scrape_headlines(url):
    print(f"--- Accessing: {url} ---")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # We look for 'h2' or 'h3' tags which usually contain headlines
        headlines = soup.find_all(['h2', 'h3'], limit=10)
        
        for i, h in enumerate(headlines):
            text = h.get_text().strip()
            if text:
                print(f"{i+1}. {text}")
                
    except Exception as e:
        print(f"Error: {e}")

# Testing with a news-focused URL (Placeholder example)
# In a real scenario, you would use this to gather text for low-resource language training.
target_url = "https://www.premiumtimesng.com/" 
scrape_headlines(target_url)
