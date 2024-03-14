import geocoder
import time
from firebase import update_location

while True:
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    print("Latitude:", latitude, "Longitude:", longitude)
    
    update_location(latitude, longitude)
    
    time.sleep(5)