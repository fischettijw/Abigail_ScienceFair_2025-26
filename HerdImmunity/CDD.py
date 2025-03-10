# use python  3.11.4
#   https://chatgpt.com/share/67b08f04-c92c-8011-90e3-967633339083

import requests

API_KEY = "TNWCYzKGlMpTMOwWlMdJkFTBFpXJgyGj"
BASE_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"

# Define headers with API key
headers = {"token": API_KEY}

# Test Request: Fetch a list of available weather stations
response = requests.get(BASE_URL, headers=headers)

if response.status_code == 200:
    print("✅ NOAA API is working!")
    print("Sample response:", response.json())  # Print a small part of the response
else:
    print("❌ API request failed! Check your API key or request format.")
    print("Error:", response.json())

for req in response.json()['results']:
    print(req['name'])