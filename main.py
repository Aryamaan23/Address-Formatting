from fastapi import FastAPI
import requests
from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import Nominatim
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

@app.get("/addressformatter/{address}")
async def addressformatter(address: str):
    results = geocoder.geocode(address)
    latitude=results[0]['geometry']['lat']
    longitude=results[0]['geometry']['lng']
    """
    print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code']))
    
    location = geolocator.reverse(str(latitude)+","+str(longitude))
    print(location)
    address = location.raw['address']
    print(address)
    """
    return {"address": address, "latitude": results[0]['geometry']['lat'], "longitude":results[0]['geometry']['lng'],"Country Code":results[0]['components']['country_code']}
