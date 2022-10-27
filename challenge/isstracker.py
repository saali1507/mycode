#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime

# access API
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    
    # SOLUTION TO PART 3
    # import datetime added above
    ts= resp["timestamp"]
    ts= datetime.datetime.fromtimestamp(ts)

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Lon: {lon}
    Lat: {lat}
    """)

if __name__ == "__main__":
    main()

