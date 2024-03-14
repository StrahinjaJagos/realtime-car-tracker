import firebase_admin
from firebase_admin import credentials, db
import os

cred = credentials.Certificate("firebase-admin.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtime-car-geolocation-default-rtdb.europe-west1.firebasedatabase.app/'
}) 

def update_location(latitude, longitude):
    ref = db.reference('/location')
    ref.update({
        'latitude': latitude,
        'longitude': longitude
    })
