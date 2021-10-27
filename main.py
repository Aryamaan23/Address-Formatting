from fastapi import FastAPI
import requests
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
from geopy.geocoders import Nominatim
from pydantic import BaseModel
from urllib.request import urlopen
import json
import FCMManager as fcm
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
app = FastAPI()
geolocator = Nominatim(user_agent="geoapiExercises")

key = 'd908ec2a841244e0892ac9b12db8a453'
geocoder = OpenCageGeocode(key)
#geo_url = 'http://maps.googleapis.com/maps/api/geocode/json'
#my_address = {'address': '21 Ramkrishana Road, Burdwan, East Burdwan, West Bengal, India', 
             #'language': 'en'}
#response = requests.get(geo_url, params = my_address)
#results = response.json()['results']
#print(results)
#my_geo = results[0]['geometry']['location']
#print("Longitude:",my_geo['lng'],"\n","Latitude:",my_geo['lat'])


 
@app.get("/")
def first_example():
    return {"Corrected Address": "Hello World!"}

@app.post("/addressformatter/")
async def addressformatter(address: str):
    results = geocoder.geocode(address)
    latitude=results[0]['geometry']['lat']
    longitude=results[0]['geometry']['lng']
    #print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        #results[0]['geometry']['lng'],
                        #results[0]['components']['country_code']))
    
    location = geolocator.reverse(str(latitude)+","+str(longitude))
    print(location)
    address = location.raw['address']
    print(address)
    
    try:
        results = geocoder.reverse_geocode(latitude, longitude, language='en', no_annotations='1')
        print(results)
        if results and len(results):
           return {"Formatted address": results[0]['formatted'],"address": address}
    except RateLimitExceededError as ex:
           print(ex)
    #URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
    #api_key = '1KA1QFOkN14SsIr0AtksGQG9RXK0dC8noQOHQrEfPf0'
    #PARAMS = {
	#		'at': '{},{}'.format(latitude,longitude),
	#		'apikey': api_key
    #    }

    # Sending get request and saving the response as response object 
    #r = requests.get(url = URL, params = PARAMS) 
  
    # Extracting data in json format 
    #data = r.json() 

    #Taking out title from JSON
    #address = data['items'][0]['title'] 
    #return {"Address with all the fields":data}

    
    #return {"address": address, "latitude": results[0]['geometry']['lat'], "longitude":results[0]['geometry']['lng'],"Country Code":results[0]['components']['country_code']}

