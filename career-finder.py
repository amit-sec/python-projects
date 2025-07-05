#This script is used to find career portal for given company name using duckduckgo websearch
#make sure to keep companies.txt in the same folder as this script and run using python3 career-finder.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote
import time
import csv

def search_duckduckgo(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "q": query + " career",
        "kl": "us-en"
    }
    response = requests.get("https://html.duckduckgo.com/html/", headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.find('a', class_='result__a')
    if not result:
        return None

    duck_link = result['href']
    parsed = urlparse(duck_link)
    real_url = unquote(parse_qs(parsed.query).get('uddg', [''])[0])

    try:
        final_url = requests.head(real_url, headers=headers, allow_redirects=True, timeout=5).url
    except:
        final_url = real_url

    return final_url

def main():
    with open('companies.txt', 'r') as f:
        companies = [line.strip() for line in f if line.strip()]

    results = []

    for company in companies:
        print(f"Searching for: {company}")
        url = search_duckduckgo(company)
        if url:
            results.append([company, url])
            print(f"✔ Found: {url}\n")
        else:
            results.append([company, "Not Found"])
            print("✘ No result found.\n")
        time.sleep(1.5)

    # Save to CSV
    with open('career_portals.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Company", "URL"])
        writer.writerows(results)

    print("✅ Results saved to career_portals.csv")

if __name__ == "__main__":
    main()
