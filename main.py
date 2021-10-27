from fastapi import FastAPI
import requests
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
from geopy.geocoders import Nominatim
from pydantic import BaseModel
from urllib.request import urlopen
import json
import FCMManager as fcm
from googletrans import Translator
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
app = FastAPI()
geolocator = Nominatim(user_agent="geoapiExercises")

key = 'd908ec2a841244e0892ac9b12db8a453'
geocoder = OpenCageGeocode(key)
translator = Translator()
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



@app.post("/addressformatterregionallanguages/")
async def addressformatter(address: str , languageoption: str):
    """
    from_lang=''
    to_lang=''
    address2=""
    address2= translator.translate({address},src= "gu",dest= "en")

   
    print(address2)
    """


    

    results = geocoder.geocode(address)
    latitude=results[0]['geometry']['lat']
    longitude=results[0]['geometry']['lng']
    #print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        #results[0]['geometry']['lng'],
                        #results[0]['components']['country_code']))
    
    location = geolocator.reverse(str(latitude)+","+str(longitude))
    print(location)
    address2 = location.raw['address']
    print(address2)
    
    #try:
    results = geocoder.reverse_geocode(latitude, longitude, language='en', no_annotations='1')
    print(results)
    x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.DEVANAGARI)
    y=transliterate(address2['amenity'], sanscript.ITRANS, sanscript.DEVANAGARI)
    z=transliterate(address2['road'], sanscript.ITRANS, sanscript.DEVANAGARI)
    a=transliterate(address2['neighbourhood'], sanscript.ITRANS, sanscript.DEVANAGARI)
    b=transliterate(address2['suburb'], sanscript.ITRANS, sanscript.DEVANAGARI)
    c=transliterate(address2['city_district'], sanscript.ITRANS, sanscript.DEVANAGARI)
    d=transliterate(address2['city'], sanscript.ITRANS, sanscript.DEVANAGARI)
    e=transliterate(address2['county'], sanscript.ITRANS, sanscript.DEVANAGARI)
    f=transliterate(address2['state_district'], sanscript.ITRANS, sanscript.DEVANAGARI)
    g=transliterate(address2['state'], sanscript.ITRANS, sanscript.DEVANAGARI)
    h=transliterate(address2['postcode'], sanscript.ITRANS, sanscript.DEVANAGARI)
    i=transliterate(address2['country'], sanscript.ITRANS, sanscript.DEVANAGARI)
    j=transliterate(address2['country_code'], sanscript.ITRANS, sanscript.DEVANAGARI)

    am= transliterate("amenity",sanscript.ITRANS, sanscript.DEVANAGARI)
    am2=transliterate("road",sanscript.ITRANS, sanscript.DEVANAGARI)
    am3=transliterate("neighbourhood",sanscript.ITRANS, sanscript.DEVANAGARI)
    am4=transliterate("suburb",sanscript.ITRANS, sanscript.DEVANAGARI)
    am5=transliterate("city_district",sanscript.ITRANS, sanscript.DEVANAGARI)
    am6=transliterate("city",sanscript.ITRANS, sanscript.DEVANAGARI)
    am7=transliterate("county",sanscript.ITRANS, sanscript.DEVANAGARI)
    am8=transliterate("state_district",sanscript.ITRANS, sanscript.DEVANAGARI)
    am9=transliterate("state",sanscript.ITRANS, sanscript.DEVANAGARI)
    am10=transliterate("postcode", sanscript.ITRANS, sanscript.DEVANAGARI)
    am11=transliterate("country",sanscript.ITRANS, sanscript.DEVANAGARI)
    am12=transliterate("country_code",sanscript.ITRANS, sanscript.DEVANAGARI)
    final_updated={"address": {
            am: y,
            am2: z,
            am3: a,
            am4: b,
            am5: c,
            am6: d,
            am7: e,
            am8: f,
            am9: g,
            am10: h,
            am11: i,
            am12: j

        }
    }
    if results and len(results):
        return {"Formatted address": x,"address": final_updated}
    #except RateLimitExceededError as ex:
          #print(ex)