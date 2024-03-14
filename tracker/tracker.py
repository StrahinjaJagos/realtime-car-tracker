import gps
import time
from firebase import update_location

gpsd = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        gps_data = gpsd.next()
        
        if gps_data['class'] == 'TPV':
            if hasattr(gps_data, 'lat') and hasattr(gps_data, 'lon'):
                latitude = gps_data.lat
                longitude = gps_data.lon
                print("Latitude:", latitude, "Longitude:", longitude)
                
                update_location(latitude, longitude)
                
    except Exception as e:
        print("Error:", e)
    
    time.sleep(5)
