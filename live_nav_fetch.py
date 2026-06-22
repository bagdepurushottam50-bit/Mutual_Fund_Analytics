live_nav_fetch.py
import requests

url = "https://www.amfiindia.com/spages/NAVAll.txt"

response = requests.get(url)

with open("nav_data.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Latest NAV data fetched successfully!")