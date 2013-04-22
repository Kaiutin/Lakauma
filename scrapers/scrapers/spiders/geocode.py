from geopy import geocoders

def oma_geocode(address):
    geocoder = geocoders.GoogleV3()
    return geocoder.geocode(address)
    
