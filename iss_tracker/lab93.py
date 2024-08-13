#!/usr/bin/env python3
import requests
import time
import reverse_geocoder as rg

URL = "http://api.open-notify.org/iss-now.json"
def main():
    resp = requests.get(URL).json()
    latitude = resp["iss_position"]["latitude"]
    longitude = resp["iss_position"]["longitude"]
    epoch = resp["timestamp"]
    timestamp = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))

    coords_tuple = (float(latitude), float(longitude))
    result = rg.search(coords_tuple, verbose=False)[0]
    country = result["cc"]
    city = result["name"]

    print("CURRENT LOCATION OF THE ISS:")
    print("Timestamp: " + timestamp)
    print("Lon: " + longitude)
    print("Lat: " + latitude)
    print("City/Country: " + city + ", " + country)

if __name__ == "__main__":
    main()