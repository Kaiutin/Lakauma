from geopy import geocoders
import time

def oma_geocode(address):
    time.sleep(0.5)
    geocoder = geocoders.GoogleV3()
    return geocoder.geocode(address)
    
