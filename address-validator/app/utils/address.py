import requests
import re

def extract_pincode(address):
    match = re.search(r"\b\d{6}\b", address)
    return match.group() if match else None

def fetch_locations(pincode):
    url = f"https://api.postalpincode.in/pincode/{pincode}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data[0]["Status"] == "Success":
            locations = []
            for post_office in data[0]["PostOffice"]:
               locations.append(f"{post_office["Name"], post_office["District"], post_office["State"]}")

            return locations
        
    return None
