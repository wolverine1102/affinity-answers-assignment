import requests
import re

def extract_pincode(address):
    match = re.search(r"\b\d{6}\b", address)
    return match.group() if match else None

def fetch_regions(pincode):
    url = f"https://api.postalpincode.in/pincode/{pincode}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data[0]["Status"] == "Success":
            regions = []
            for post_office in data[0]["PostOffice"]:
               regions.append({
                   "area" : post_office["Name"].lower(),
                   "district" : post_office["District"].lower()
               })
            return regions
        
    return None
